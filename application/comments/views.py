from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from application import app, db
from application.auth.models import User
from application.memes.models import Meme

# running out of time thanks to excellent procrastinating skills
# to be implemented later

# comments can be submitted on individual meme entries
# comments cannot be modified, only deleted
# comments can only be submitted by logged in users

@app.route("/comments/new/")
@login_required
def comments_form():
    return render_template("comments/new.html", form = CommentForm())