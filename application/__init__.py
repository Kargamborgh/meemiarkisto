from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///memes.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'blblblblblbl'

from application import views

from application.memes import models
from application.memes import views

from application.auth import models

db.create_all()