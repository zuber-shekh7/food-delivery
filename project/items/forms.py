from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,SelectField,TextAreaField,RadioField,IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired,Length,EqualTo

class CreateItemForm(FlaskForm):

    name = StringField('enter name',validators=[DataRequired()])
    price = IntegerField('enter price',validators=[DataRequired()])
    quantity = IntegerField('enter quantity',validators=[DataRequired()])
    unit = StringField('enter unit',validators=[DataRequired()])
    type = SelectField('select type',validators=[DataRequired()],choices=[('veg','veg'),('non-veg','non-veg')])
    description = TextAreaField('description')
    is_avaliable = RadioField('is avaliable',choices=[('yes','yes'),('no','no')])