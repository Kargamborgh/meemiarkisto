from application import db
from application.models import Base
# these below are not currently in use, futureproofing for added security
from werkzeug.security import generate_password_hash, check_password_hash

# users can submit memes and leave comments which are both tied to their
# individual user accounts

class User(Base):

    __tablename__ = "account"
  
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), index=True, nullable=False)
    password = db.Column(db.String(144), nullable=False)
    #password_hash = db.Column(db.String(128)) this will be implemented later

    meme_id = db.relationship("Meme", backref='account', lazy=True)
    comment_id = db.relationship("Comment", backref='comment', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)