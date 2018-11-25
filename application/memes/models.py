from application import db

# A meme has id as primary key, a creation (upload) date, a title and upvotes/downvotes shown as points
# Later a meme will also have fields for comments, who uploaded it etc.

class Meme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    title = db.Column(db.String(144), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    #image = db.Column(db.LargeBinary) <-- this currently fucks everything up, commented out for now

    def __init__(self, title):
        self.title = title
        self.points = 0
