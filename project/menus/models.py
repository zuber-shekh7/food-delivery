from project.app import db,bcrypt,login_manager
# from project.items.models import Item

class Menu(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    items = db.relationship('Item',backref='menu',lazy=True)
    restaurant_id = db.Column(db.Integer,db.ForeignKey('restaurants.id'),nullable=False)
    
    def __init__(self,name,restaurant_id):
        self.name = name
        self.restaurant_id = restaurant_id

    def __str__(self):
        return f'{self.name}'