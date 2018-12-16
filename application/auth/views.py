from flask import render_template, request, redirect, url_for, session
from flask_login import login_user, logout_user, current_user
  
from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm
from application.memes.models import Meme

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # validations go here

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")


    login_user(user)
    session["most_memes"] = Meme.find_most_memes_user()
    session["most_comments"] = Meme.find_most_comments_user()
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form=RegisterForm())

    form = RegisterForm()

    # WTForms validators in auth/forms.py
    u = User(name=form.name.data,
                 username=form.username.data,
                 password=form.password.data)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("auth_login"))