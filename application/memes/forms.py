from flask_wtf import FlaskForm
from wtforms import FileField, StringField, validators

# user interaction in meme submission is limited to file(image) and a title

class MemeForm(FlaskForm):

    image = FileField('Image', nullable=False)
    title = StringField('Image description', [validators.Length(min=3)], nullable=False)
    