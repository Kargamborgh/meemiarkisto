from flask_wtf import FlaskForm
from wtforms import FileField, StringField, validators

class MemeForm(FlaskForm):
    image = FileField('Image') ## implement image validation when you have a chance
    title = StringField('Image description', [validators.Length(min=3)])