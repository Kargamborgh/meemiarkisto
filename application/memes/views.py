import os
from application import app, db
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from flask_uploads import configure_uploads, UploadSet, UploadConfiguration
from application.memes.models import Meme
from application.memes.forms import MemeForm
from application.auth.models import User

# config for file upload
images = UploadSet('images', extensions=('jpg','jpeg','png'),)

@app.route("/memes", methods=["GET"])
def memes_index():
    return render_template("memes/list.html", memes = Meme.query.all())

@app.route("/memes/new/")
@login_required
def memes_form():
    return render_template("memes/new.html", form = MemeForm())

@app.route("/memes/<meme_id>/", methods=["POST"])
@login_required
def memes_increase_score(meme_id):

    m = Meme.query.get(meme_id)
    m.points = m.points+1
    db.session().commit()

    return redirect(url_for("memes_index"))

def memes_decrease_score(meme_id):

   m = Meme.query.get(meme_id)
   m.points = m.points-1
   db.session().commit()

   return redirect(url_for("memes_index"))

# this image upload is tricky, still broken
@app.route("/memes/", methods=["POST"])
@login_required
def memes_create():
    form = MemeForm(request.form)
    if 'image' in request.files:
        filename = images.save(request.files['image'])
        rec = image(filename=filename, user=current_user.id)
        rec.store()
        flash("Image saved.")
        return redirect(url_for("memes_index", id=rec.id))
    return render_template('memes/new.html')

    if not form.validate():
        return render_template("memes/new.html", form = form)

    m = Meme(title=form.title.data, points=0, date_created=db.func.current_timestamp())
    m.account_id = current_user.id

    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("memes_index"))