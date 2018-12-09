from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired

# a comment is just a text string submitted on a meme entry

class CommentForm(FlaskForm):
    text = TextField("Comment", validators=[DataRequired()])
    submit = SubmitField('Submit')

    class Meta:
        csrf = False