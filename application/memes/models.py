from application import db, app
from application.models import Base

from flask_uploads import configure_uploads

# A meme consist of an image, a title, points, filename (when uploading),
# id of user who uploaded the meme, 0-* comments
# A meme image will later be served from '/images' to correspond to a meme entry

class Meme(Base):

    __tablename__ = "meme"

    # image field & upload is still under construction
    # image = file
    title = db.Column(db.String(144), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    filename = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    # comment table breaks things because of emptiness and relationships, commented out for now
    # comment_id = db.relationship("Comment", backref="comment", lazy=True)


    def __init__(self, title, points, date_created):
        self.title = title
        self.points = 0
        self.date_created = date_created

    def __repr__(self):
        return '<Meme {}>'.format(self.title)