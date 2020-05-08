from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired,Length,EqualTo

class CreateMenuForm(FlaskForm):

    name = StringField('enter name',validators=[DataRequired()])