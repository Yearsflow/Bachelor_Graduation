from app import app,db
from app.tables import administrator,users
from flask import render_template,request,flash,redirect,url_for
from flask_login import current_user,login_user,logout_user,login_required
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
                if is_admin:
                    return render_template('admin.html')
                else:
                    return render_template('user.html')
            flash(error)
        if submit_register=='submit':
            data=users(Name=UserName,Email=Email,Password=Password)
            db.session.add(data)
            db.session.commit()
            flash('注册成功！')
    return render_template('login.html')