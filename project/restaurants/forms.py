from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired,Length,EqualTo

class SignupForm(FlaskForm):

    email = EmailField('enter email',validators=[DataRequired()])
    fname = StringField('enter firstname',validators=[DataRequired()])
    lname = StringField('enter lastname',validators=[DataRequired()])
    mobile = StringField('enter mobile',validators=[DataRequired(),Length(max=10)])