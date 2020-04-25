from project.app import db,bcrypt,login_manager
from project.items.models import Item

class Menu(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    restaurant_id = db.Column(db.Integer,db.ForeignKey('restaurant.id'),nullable=False)
    items = db.relationship('Item',backref='menu',lazy=True,cascade='all,delete')
    

    def __str__(self):
        return f'{self.name}'