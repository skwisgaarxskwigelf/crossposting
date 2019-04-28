from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError


from ..models import Channel

class ChannelsForm():
    """
    Form to add and edit channels
    """
    name = StringField('Name')
    submit = SubmitField('Submit')
