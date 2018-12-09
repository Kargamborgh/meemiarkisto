from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.auth.models import User
from application.memes.models import Meme
from application.comments.forms import CommentForm

# only a dummy new comment form

@app.route("/comments/new/")
@login_required(role="ANY")
def comments_form():
    return render_template("comments/new.html", form = CommentForm())