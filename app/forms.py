
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length

class ExampleForm(FlaskForm):
    field = TextAreaField('Example', validators=[DataRequired()])
    submit = SubmitField('Submit')
