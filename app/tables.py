from app import db,login
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    t=users.query.get(int(user_id))
    if int(user_id)>=100:
        return administrator.query.get(int(user_id))
    else:
        return t

class administrator(UserMixin,db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    Name=db.Column(db.String(10),nullable=False)
    Email=db.Column(db.String(20),nullable=False)
    Password=db.Column(db.Text,nullable=False)
    def get_id(self):
        return self.Id
    def check_password(self,password):
        return self.Password==password
    def set_password(self,password):
        self.Password=password

class users(UserMixin,db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    Name=db.Column(db.String(8),nullable=False)
    Email=db.Column(db.String(20),nullable=False)
    Password=db.Column(db.Text,nullable=False)
    def get_id(self):
        return self.Id
    def check_password(self,password):
        return self.Password==password
    def set_password(self,password):
        self.Password=password

class news(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    Category=db.Column(db.String(20),nullable=False)
    Content=db.Column(db.Text,nullable=False)
    def get_id(self):
        return self.Id

class favorite(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    UserId=db.Column(db.Integer,db.ForeignKey('users.Id'),nullable=False)
    NewsId=db.Column(db.Integer,db.ForeignKey('news.Id'),nullable=False)
    def get_id(self):
        return self.Id