from application import db
from application.models import Base

# A meme has id as primary key, a creation (upload) date, a title and upvotes/downvotes shown as points
# Later a meme will also have fields for comments, who uploaded it etc.

class Meme(Base):

    __tablename__ = "meme"

    title = db.Column(db.String(144), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    #image = db.Column(db.LargeBinary) <-- this currently messes everything up, commented out for now

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, title, points, date_created):
        self.title = title
        self.points = 0
        self.date_created = date_created

    def __repr__(self):
        return '<Meme {}>'.format(self.title)
