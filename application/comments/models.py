from application import db
from application.models import Base

class Comment(Base):

    __tablename__ = "comment"
    
    text = db.Column(db.String(280), nullable=False) # tweet length should be fine

    # a comment belongs to the user that wrote it
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    # a comment is written on any single meme entry
    memes = db.Column(db.Integer, db.ForeignKey("meme.id"), nullable=False)