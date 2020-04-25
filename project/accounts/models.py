from project.app import db,bcrypt,login_manager
from flask_login import UserMixin
from project.restaurants.models import Restaurant

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(),nullable=False)
    password = db.Column(db.String(),nullable=False)
    fname = db.Column(db.String(),nullable=False)
    lname = db.Column(db.String(),nullable=False)
    moblie = db.Column(db.String(),nullable=False)
    is_admin = db.Column(db.Boolean(),default=False,nullable=False)
    restaurants = db.relationship('Restaurant',backref='user',lazy=True)
    
    def __init__(self,email,password,fname,lname,moblie):
        self.email=email
        self.password=bcrypt.generate_password_hash(password)
        self.fname=fname
        self.lname=lname
        self.moblie=moblie

    def __str__(self):
        return f'{self.email}'

    def check_password(self,password):
        return bcrypt.check_password_hash(self.password,password)