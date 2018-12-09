from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired

# a comment is just a text string submitted on a meme entry

#class CommentForm(FlaskForm):
#    text = TextField("Text", validators=[DataRequired()])