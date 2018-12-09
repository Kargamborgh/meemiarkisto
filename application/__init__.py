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

# flask-uploads
from flask_uploads import configure_uploads, UploadSet, patch_request_class, IMAGES
app.config['UPLOADED_IMAGES_DEST'] = '/static/images'
app.config['UPLOADS_DEFAULT_URL'] = 'http://localhost:5000/static/images/'
images = UploadSet('images', IMAGES)
configure_uploads(app, images)
patch_request_class(app, 2 * 1024 * 1024 ) #set maximum filesize to 2 megabytes

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