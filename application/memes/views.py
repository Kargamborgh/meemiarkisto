import os
from flask_login import current_user, login_required
from application import app, db, login_required
from flask import flash, redirect, render_template, request, url_for, session
from flask_uploads import configure_uploads, UploadSet, patch_request_class
from application.memes.models import Meme
from application.memes.forms import MemeForm
from application.auth.models import User
from application.comments.models import Comment
from application.comments.forms import CommentForm
from helpers import s3

from sqlalchemy import text

# by definition all memes are public and visible to all users

@app.route("/memes", methods=["GET"])
def memes_index():
    return render_template("memes/list.html", memes = Meme.query.all())

# join meme & user tables to display author in single meme view
# also join meme and comment tables to print relevant comments in meme view
@app.route("/memes/<meme_id>", methods=["GET"])
def meme_view(meme_id):

# make meme_comments in global context to enable easy printing in meme view
# comments are anonymous but most prolific commenters are visible in index.html

    session.meme_comments = db.session.query(Comment.text).filter(Comment.meme_id == meme_id)
    
    meme_with_user_and_comments = db.session.query(Meme, User, Comment).join(User, Comment).filter(Meme.id == meme_id).first()
    
    return render_template("memes/view.html", meme = meme_with_user_and_comments, form=CommentForm())

@app.route("/memes/new/")
@login_required(role="ANY")
def memes_form():
    return render_template("memes/new.html", form = MemeForm())

# TODO rework upvote/downvote to return a redirect to current path
# as opposed to throwing user back to memes_index

@app.route("/memes/upvote/<meme_id>/", methods=["POST"])
@login_required(role="ANY")
def memes_increase_score(meme_id):

    meme = Meme.query.get(meme_id)
    meme.points = meme.points+1
    db.session().commit()

    return redirect(url_for("memes_index"))

@app.route("/memes/downvote/<meme_id>/", methods=["POST"])
@login_required(role="ANY")
def memes_decrease_score(meme_id):

   meme = Meme.query.get(meme_id)
   meme.points = meme.points-1
   db.session().commit()

   return redirect(url_for("memes_index"))

# delete a meme from the database

@app.route("/memes/delete/<meme_id>/", methods=["POST"])
@login_required(role="ANY")
def memes_delete(meme_id):
    statement = text("DELETE FROM meme WHERE id = :id").params(id=meme_id)
    db.engine.execute(statement)
    db.session().commit()

    return redirect(url_for("memes_index"))

# AWS S3 bucket upload method, used in memes_create() below
# returns URL for uploaded image

def upload_file_to_s3(file, bucket_name, acl="public-read"):

        s3.upload_fileobj(
                file,
                bucket_name,
                file.filename,
                ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
                }
        )
        return "https://s3.eu-north-1.amazonaws.com/meemiarkistobucket/{}".format(file.filename)

# add a new meme, including an image

@app.route("/memes/", methods=["POST"])
@login_required(role="ANY")
def memes_create():
    form = MemeForm()

    if form.validate_on_submit():
        file = request.files["image"] # get image file from request
        url = upload_file_to_s3(file, "meemiarkistobucket") # use method above to upload
        meme = Meme(form.title.data, 0, file.filename, url, current_user.id) # add meme details to database

        db.session().add(meme)
        db.session().commit()

    return redirect(url_for("memes_index"))

# add a comment to a meme, maybe this is easier here than at comments/views

@app.route("/memes/comment/<meme_id>/", methods=["POST"])
@login_required(role="ANY")
def memes_comment(meme_id):
    form = CommentForm()
    meme = Meme.query.get(meme_id)

    if form.validate_on_submit():
        comment = Comment(form.text.data, current_user.id, meme.id)
        
        db.session().add(comment)
        db.session().commit()
        
    return redirect(url_for("memes_index"))
