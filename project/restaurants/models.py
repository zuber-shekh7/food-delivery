from project.app import db,bcrypt,login_manager
from project.menus.models import Menu


class Restaurant(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    owner = db.Column(db.String,nullable=False)
    email = db.Column(db.String,nullable=False)
    mobile = db.Column(db.String,nullable=False)
    license = db.Column(db.String,nullable=False)
    is_open = db.Column(db.Boolean,default=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),unique=True)
    menus = db.relationship('Menu',backref='restaurant',lazy=True)

    def __str__(self):
        return f'{self.name}'

