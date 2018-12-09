import os
from application import app, db, images, login_required
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user
from flask_uploads import configure_uploads, UploadSet, patch_request_class
from application.memes.models import Meme
from application.memes.forms import MemeForm
from application.auth.models import User

from sqlalchemy import text

# by definition all memes are public and visible to all users

@app.route("/memes", methods=["GET"])
def memes_index():
    return render_template("memes/list.html", memes = Meme.query.all())

# join meme & user tables to display author in single meme view
@app.route("/memes/<meme_id>", methods=["GET"])
def meme_view(meme_id):
    meme_with_user = db.session.query(Meme, User).join(User).filter(Meme.id == meme_id).first()
    return render_template("memes/view.html", meme = meme_with_user)

@app.route("/memes/new/")
@login_required(role="ANY")
def memes_form():
    return render_template("memes/new.html", form = MemeForm())

# TODO rework upvote/downvote to return a redirect to current path
# as opposed to throwing user back to memes_index

@app.route("/memes/upvote/<meme_id>/", methods=["POST"])
@login_required(role="ANY")
def memes_increase_score(meme_id):

    m = Meme.query.get(meme_id)
    m.points = m.points+1
    db.session().commit()

    return redirect(url_for("memes_index"))

@app.route("/memes/downvote/<meme_id>/", methods=["POST"])
@login_required(role="ANY")
def memes_decrease_score(meme_id):

   m = Meme.query.get(meme_id)
   m.points = m.points-1
   db.session().commit()

   return redirect(url_for("memes_index"))

@app.route("/memes/delete/<meme_id>/", methods=["POST"])
@login_required(role="ANY")
def memes_delete(meme_id):
    statement = text("DELETE FROM meme WHERE id = :id").params(id=meme_id)
    db.engine.execute(statement)
    db.session().commit()

    return redirect(url_for("memes_index"))

@app.route("/memes/", methods=["POST"])
@login_required(role="ANY")
def memes_create():
    form = MemeForm()

    # handle image upload here
    if form.validate_on_submit():
        print('conels')
        filename = images.save(request.files['image'])
        url = images.url(filename)
        m = Meme(form.title.data, 0, filename, url, current_user.id)

        # else: save image and meme details to database
        db.session().add(m)
        db.session().commit()
        flash("Image saved.")

        return redirect(url_for("memes_index"))
    else:
        flash('error: meme not added', 'error')
        return render_template('memes/new.html', form=form)