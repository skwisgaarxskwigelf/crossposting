from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, validators, ValidationError


class ChannelsForm(FlaskForm):
    """
    Form to add and edit channels
    """
    name = StringField('Name', [validators.Length(min=1, max=35)])
    telegram_chat_id = StringField('Channel id', [validators.Length(min=1, max=35)])
    is_active = BooleanField('Active')
    submit = SubmitField('Submit')