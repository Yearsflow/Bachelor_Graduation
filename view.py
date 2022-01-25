from flask import Flask,render_template,request,flash,redirect,url_for
from flask_login import current_user,login_user,logout_user,login_required
from importlib_metadata import re
from markupsafe import escape
from config import Config
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        UserName=request.form.get('logname')
        Password=request.form.get('logpass')
        

if __name__=='__main__':
    app.run(debug=True)