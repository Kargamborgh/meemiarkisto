# flask app
from flask import Flask
app = Flask(__name__)

# local database stuff
from flask_sqlalchemy import SQLAlchemy

import os

# database switch depending on heroku/local
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///memes.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# application functionality
from application import views

from application.memes import models
from application.memes import views

from application.auth import models
from application.auth import views

# login stuff

from application.auth.models import User
from os import urandom
app.config['SECRET_KEY'] = urandom(32) # SUPER SECRET CSRF KEY DO NOT STEAL

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# create database tables if needed
try:
    db.create_all()
except:
    pass