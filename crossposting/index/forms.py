from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class ChannelsForm():
    """
    Form to add and edit channels
    """
    name = StringField('Name')
    submit = SubmitField('Submit')
