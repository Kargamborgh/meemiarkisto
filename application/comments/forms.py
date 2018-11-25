from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    text = TextField("Text", validators=[DataRequired()])