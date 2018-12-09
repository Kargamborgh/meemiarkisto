from application import db, app
from application.models import Base

from flask_uploads import configure_uploads

# A meme consist of an image, a title, points, filename,
# id of user who uploaded the meme, 0-* comments

class Meme(Base):

    __tablename__ = "meme"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(144), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    filename = db.Column(db.String(144), nullable=True)
    url = db.Column(db.String(144), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)


    def __init__(self, title, points, filename, url, account_id):
        self.title = title
        self.points = points
        self.filename = filename
        self.url = url
        self.account_id = account_id

    def __repr__(self):
        return '<Meme {}>'.format(self.title)