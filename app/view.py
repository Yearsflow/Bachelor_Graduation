from urllib.parse import urlparse
from app import app,db
from app.tables import administrator,users
from flask import render_template,request,flash,redirect,url_for
from flask_login import current_user,login_user,logout_user,login_required,login_manager
from importlib_metadata import re
from markupsafe import escape
from .config import Config
from flask_sqlalchemy import SQLAlchemy

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

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

@app.route('/admin_index')
@login_required
def admin_index():
    if isinstance(current_user._get_current_object(),administrator):
        return render_template('admin.html')
    else:
        logout_user()

@app.route('/user_index')
@login_required
def user_index():
    if isinstance(current_user._get_current_object(),users):
        return render_template('user.html')
    else:
        logout_user()