from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from app.models import Gamestop


# Create your forms here.
class GamestopForm(FlaskForm):
    """Form for adding/updating a Gamestop."""
    # TODO: Add the following fields to the form class:
    # - title - StringField
    title = StringField('Title', validators=[DataRequired()])
    # - address - StringField
    address = StringField('Address', validators=[DataRequired()])
    # - submit button
    submit = SubmitField('Submit')

class GameForm(FlaskForm):
    """Form for adding/updating a Game."""
    # TODO: Add the following fields to the form class:
    # - title - StringField
    name = StringField('Name', validators=[DataRequired()])
    # - address - StringField
    photo_url = StringField('Photo URL', validators=[DataRequired()])

    gamestop = QuerySelectField('Gamestop', query_factory=lambda: Gamestop.query, allow_blank=False)
    # - submit button
    submit = SubmitField('Submit')

