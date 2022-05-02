from urllib.parse import urlparse
from graphviz import render
from numpy import isin
from app import app,db
from app.tables import administrator,users,news,favorite
from flask import render_template,request,flash,redirect,url_for
from flask_login import current_user,login_user,logout_user,login_required,login_manager
from importlib_metadata import re
from markupsafe import escape
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from snownlp import SnowNLP
from .filter import DFAFilter
import joblib
from . import pipeline
import json

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/clean',methods=['GET','POST'])
@login_required
def clean():
    if request.method=='GET':
        if isinstance(current_user._get_current_object(),administrator):
            return render_template('clean.html')
        else:
            logout_user()
            return redirect(url_for('login'))
    if request.method=='POST':
        text=request.form.get('clean_text')
        text=pipeline.clean(text)
        clean_button=request.form.get('clean')
        if clean_button=='clean':
            return render_template('clean.html',data=text)
        return redirect(url_for('admin_index'))

@app.route('/vector',methods=['GET','POST'])
@login_required
def vector():
    if request.method=='GET':
        if isinstance(current_user._get_current_object(),administrator):
            return render_template('vector.html')
        else:
            logout_user()
            return redirect(url_for('login'))
    if request.method=='POST':
        text=request.form.get('vector_text')
        tfidf=pipeline.vectorize(text).toarray()
        res=''
        for i in range(len(tfidf)):
            for j in range(len(tfidf[i])):
                res+=str(tfidf[i][j])+','
        vector_button=request.form.get('vector')
        if vector_button=='vector':
            return render_template('vector.html',data=res)
        return redirect(url_for('admin_index'))

@app.errorhandler(404)
def error(e):
    return render_template('404.html'),404

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        if isinstance(current_user._get_current_object(),administrator):
            return redirect(url_for('admin_index'))
        elif isinstance(current_user._get_current_object(),users):
            return redirect(url_for('user_index'))
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        UserName=request.form.get('logname')
        Email=request.form.get('logemail')
        Password=request.form.get('logpass')
        submit_login=request.form.get('submit-login')
        submit_register=request.form.get('submit-register')
        if submit_login=='submit':
            error=None
            is_admin=False
            user=users.query.filter_by(Name=UserName,Email=Email).first()
            if not user:
                is_admin=True
                user=administrator.query.filter_by(Name=UserName,Email=Email).first()
            if not user:
                error='用户不存在！'
            elif not user.check_password(Password):
                error='密码错误！'
            if error is None:
                login_user(user)
                next_page=request.args.get('next')
                if not next_page or urlparse(next_page).netloc!='':
                    next_page=url_for('index')
                if is_admin:
                    return redirect(url_for('admin_index'))
                else:
                    return redirect(url_for('user_index'))
            flash(error)
        if submit_register=='submit':
            data=users(Name=UserName,Email=Email,Password=Password)
            db.session.add(data)
            db.session.commit()
            flash('注册成功！')
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/admin_index',methods=['GET','POST'])
@login_required
def admin_index():
    if request.method=='GET':
        if isinstance(current_user._get_current_object(),administrator):
            articles=news.query.limit(100).all()
            for i in range(len(articles)):
                articles[i].Content=articles[i].Content.strip('\r')
            return render_template('admin.html',articles=articles)
        else:
            logout_user()
            return redirect(url_for('login'))
    if request.method=='POST':
        submit_logout=request.form.get('logout')
        if submit_logout=='logout':
            logout_user()
            return redirect(url_for('login'))

@app.route('/user_index',methods=['GET','POST'])
@login_required
def user_index():
    if request.method=='GET':
        if isinstance(current_user._get_current_object(),users):
            articles=news.query.limit(100).all()
            CollectionNews=favorite.query.filter_by(UserId=current_user.Id).all()
            for i in range(len(articles)):
                articles[i].Content=articles[i].Content.strip('\r')
            return render_template('user.html',articles=articles,CollectionNews=CollectionNews)
        else:
            logout_user()
            return redirect(url_for('login'))
    if request.method=='POST':
        data = json.loads(request.form.get('data'))
        news_id = data['id']
        flag = data['flag']
        if (flag):
            record = favorite(UserId=current_user.Id, NewsId=news_id)
            db.session.add(record)
            db.session.commit()
        else:
            db.session.query(favorite).filter(favorite.UserId == current_user.Id, favorite.NewsId == news_id).delete()
            db.session.commit()
        submit_logout=request.form.get('logout')
        if submit_logout=='logout':
            logout_user()
            return redirect(url_for('login'))
        return redirect(url_for('user_index'))

@app.route('/emotional',methods=['GET','POST'])
@login_required
def emotional():
    if request.method=='GET':
        if isinstance(current_user._get_current_object(),users):
            return render_template('emotional.html')
        else:
            logout_user()
            return redirect(url_for('login'))
    if request.method=='POST':
        text=request.form.get('emotional_text')
        s=SnowNLP(text)
        emotional_button=request.form.get('emotional')
        if emotional_button=='analyze':
            return render_template('emotional.html',data=s)
        return redirect(url_for('user_index'))

@app.route('/detect',methods=['GET','POST'])
@login_required
def detect():
    if request.method=='GET':
        if isinstance(current_user._get_current_object(),users):
            return render_template('detect_user.html')
        elif isinstance(current_user._get_current_object(),administrator):
            return render_template('detect_admin.html')
        else:
            logout_user()
            return redirect(url_for('login'))
    if request.method=='POST':
        text=request.form.get('detect_text')
        gfw=DFAFilter()
        gfw.parse('./train_text_data/sensitive_words.txt')
        result=gfw.filter(text,"*")
        flag=False
        for i in result:
            if i=='*':
                flag=True
                break
        detect_button=request.form.get('detect')
        if detect_button=='detect':
            if isinstance(current_user._get_current_object(),users):
                return render_template('detect_user.html',data=result,flag=flag)
            if isinstance(current_user._get_current_object(),administrator):
                return render_template('detect_admin.html',data=result)
        if isinstance(current_user._get_current_object(),users):
            return redirect(url_for('user_index'))
        if isinstance(current_user._get_current_object(),administrator):
            return redirect(url_for('admin_index'))

@app.route('/classify',methods=['GET','POST'])
@login_required
def classify():
    if request.method=='GET':
        if isinstance(current_user._get_current_object(),users):
            return render_template('classify.html')
        else:
            logout_user()
            return redirect(url_for('login'))
    if request.method=='POST':
        text=request.form.get('classify_text')
        classifier=request.form.get('classifier')
        result=pipeline.predict_label(classifier,text)
        classify_button=request.form.get('classify')
        if classify_button=='classify':
            return render_template('classify.html',data=result)
        return redirect(url_for('user_index'))

@app.route('/user_info/<int:change>',methods=['GET','POST'])
@app.route('/user_info',defaults={'change':0},methods=['GET','POST'])
@login_required
def user_info(change):
    if request.method=='POST':
        old_password=request.form['oldpassword']
        new_password=request.form['newpassword']
        new_password2=request.form['newpassword2']
        if not new_password==new_password2:
            flash('两次密码输入不一致！')
        elif not current_user.check_password(old_password):
            flash('原密码输入错误！')
        else:
            current_user.set_password(new_password)
            db.session.commit()
            flash('Your changes have been saved.')
        return redirect(url_for('user_info'))
    return render_template('user_info.html',change=change)

@app.route('/keywords',methods=['GET','POST'])
@login_required
def keywords():
    if request.method=='GET':
        return render_template('keywords.html')
    if request.method=='POST':
        text=request.form.get('news_text')
        keywords=pipeline.keywords(text)
        extract_button=request.form.get('extract')
        if extract_button=='extract':
            return render_template('keywords.html',data=keywords)
        return redirect(url_for('admin_index'))

@app.route('/show',methods=['GET','POST'])
@login_required
def show():
    if request.method=='GET':
        if isinstance(current_user._get_current_object(),users):
            return render_template('show.html')
        else:
            logout_user()
            return redirect(url_for('login'))
    return redirect(url_for('user_index'))

@app.route('/predict',methods=['GET','POST'])
@login_required
def predict():
    if request.method=='GET':
        return render_template('predict.html')