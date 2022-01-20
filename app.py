from flask import Flask,render_template,request,flash,redirect,url_for
from flask_login import current_user,login_user,logout_user,login_required
from markupsafe import escape

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/login',methods=['GET','POST'])
def login():
    if isinstance(current_user._get_current_object(),Administrator):
        logout_user()

if __name__=='__main__':
    app.run(debug=True)