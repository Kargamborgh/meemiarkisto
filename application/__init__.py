# imports
import os

# flask app
from flask import Flask
app = Flask(__name__)

# local database stuff
from flask_sqlalchemy import SQLAlchemy

# database switch depending on heroku/local
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///memes.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# S3 uploads stuff

S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
S3_KEY = os.environ.get("AWS_ACCESS_KEY_ID")
S3_SECRET = os.environ.get("AWS_SECRET_ACCESS_KEY")
S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)


# login stuff

from os import urandom
app.config['SECRET_KEY'] = urandom(32) # SUPER SECRET CSRF KEY DO NOT STEAL

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles stuff, any/user/admin
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated():
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# load application
from application import views

from application.memes import models
from application.memes import views

from application.auth import models
from application.auth import views

from application.comments import models
from application.comments import views

# more login stuff

from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# create database tables if needed
try:
    db.create_all()
except:
    pass