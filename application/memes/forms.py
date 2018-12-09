from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired
from application import images

# user interaction in meme submission is limited to file(image) and a title

class MemeForm(FlaskForm):

    title = StringField('Image description', [validators.Length(min=3)])
    image = FileField('Image', validators=[FileRequired(), FileAllowed(images,)])
    submit = SubmitField('Submit new meme')

    class Meta:
        csrf = False
    