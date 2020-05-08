from project.app import db,bcrypt,login_manager


class Item(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    price = db.Column(db.Integer,nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    unit = db.Column(db.String,default='number',nullable=False)
    type = db.Column(db.String,default='veg',nullable=False)
    desc = db.Column(db.String,nullable=True)
    is_avaiable = db.Column(db.Boolean,default=True)
    menu_id = db.Column(db.Integer,db.ForeignKey('menu.id'),nullable=False)

    def __init__(self,name,price,quantity,unit,type,desc,is_avaiable,menu_id):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.unit = unit
        self.type = type
        self.desc = desc
        self.is_avaiable = True if is_avaiable else False
        self.menu_id = menu_id

    def __str__(self):
        return f'{self.name}'