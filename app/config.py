import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "I-don't-know!"
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:tyc0520!@localhost:3306/bachelor_graduation?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS=True