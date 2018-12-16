from application import db, app
from application.models import Base

from sqlalchemy.sql import text

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

    @staticmethod
    def find_most_memes_user():
        statement = text("SELECT account.username AS username, COUNT(meme.account_id) AS amount "
        "FROM meme INNER JOIN account ON meme.account_id = account.id "
        "GROUP BY username ORDER BY amount DESC")
        retd = db.engine.execute(statement)
        response = []
        for row in retd:
            response.append({"username":row[0], "amount":row[1]})

        return response

    @staticmethod
    def find_most_comments_meme():
        statement = text("SELECT meme.title AS name, COUNT(comment.meme_id) AS comments "
        "FROM comment INNER JOIN meme ON comment.meme_id = meme.id "
        "GROUP BY meme.title ORDER BY comments DESC")
        retd = db.engine.execute(statement)
        response = []
        for row in retd:
            response.append({"name":row[0], "comments":row[1]})

        return response