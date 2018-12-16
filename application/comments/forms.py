from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired

# a comment is just a text string submitted on a meme entry

class CommentForm(FlaskForm):
    text = StringField("Comment", [validators.Length(min=3)])
    submit = SubmitField('Submit')

    class Meta:
        csrf = False