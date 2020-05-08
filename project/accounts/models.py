from project.app import db,bcrypt,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model,UserMixin):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(),nullable=False)
    password = db.Column(db.String(),nullable=False)
    fname = db.Column(db.String(),nullable=False)
    lname = db.Column(db.String(),nullable=False)
    moblie = db.Column(db.String(10),nullable=False)
    type = db.Column(db.String(),default='user',nullable=False)
    is_admin = db.Column(db.Boolean(),default=False,nullable=False)
    restaurant = db.relationship('Restaurant',backref='owner',lazy=True)
    address = db.relationship('Address',backref='user',lazy=True)

    def __init__(self,email,password,fname,lname,moblie,type):
        self.email=email
        self.password=bcrypt.generate_password_hash(password)
        self.fname=fname
        self.lname=lname
        self.moblie=moblie
        self.type=type

    def __str__(self):
        return f'{self.email}'

    def check_password(self,password):
        return bcrypt.check_password_hash(self.password,password)

class Address(db.Model):

    __tablename__ = 'addresses'

    id = db.Column(db.Integer,primary_key=True)
    flat_no = db.Column(db.Integer,nullable=False)
    landmark = db.Column(db.String,nullable=False) 
    city = db.Column(db.String,nullable=False) 
    state = db.Column(db.String,nullable=False) 
    country = db.Column(db.String,nullable=False) 
    pincode = db.Column(db.String(6),nullable=False) 
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),unique=True)
    

    def __str__(self):
        return f'{self.flat_no},{self.landmark},{self.city},{self.state},{self.pincode}'