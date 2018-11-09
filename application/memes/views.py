from application import app, db
from flask import redirect, render_template, request, url_for
from application.memes.models import Meme

@app.route("/memes", methods=["GET"])
def memes_index():
    return render_template("memes/list.html", memes = Meme.query.all())

@app.route("/memes/new/")
def memes_form():
    return render_template("memes/new.html")

@app.route("/memes/<meme_id>/", methods=["POST"])
def memes_increase_score(meme_id):

    m = Meme.query.get(meme_id)
    m.points = m.points+1
    db.session().commit()

    return redirect(url_for("memes_index"))

# Implement this next week

#@app.route("/memes/<meme_id>/", methods=["POST"])
#def memes_decrease_score(meme_id):

#    m = Meme.query.get(meme_id)
#    m.points =-1
#    db.session().commit()

#    return redirect(url_for("memes_index"))

@app.route("/memes/", methods=["POST"])
def memes_create():
    m = Meme(request.form.get("title"))
    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("memes_index"))