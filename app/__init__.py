from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_login import LoginManager

app=Flask(__name__)
app.config.from_object(Config)
login=LoginManager(app)
login.login_view='login'
db=SQLAlchemy(app)

from app import view,tables