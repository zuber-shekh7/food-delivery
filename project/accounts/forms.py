from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired,Length,EqualTo


class LoginForm(FlaskForm):

    email = EmailField('enter email',validators=[DataRequired()])
    password = PasswordField('enter password',validators=[DataRequired()])

class SignupForm(FlaskForm):

    email = EmailField('enter email',validators=[DataRequired()])
    password = PasswordField('enter password',validators=[DataRequired()])
    cpassword = PasswordField('confirm password',validators=[DataRequired(),EqualTo('password')])
    fname = StringField('enter firstname',validators=[DataRequired()])
    lname = StringField('enter lastname',validators=[DataRequired()])
    mobile = StringField('enter mobile',validators=[DataRequired(),Length(max=10)])