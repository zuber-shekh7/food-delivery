from project.app import db,bcrypt,login_manager


class Item(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    quantity = db.Column(db.String,nullable=False)
    price = db.Column(db.Integer,nullable=False)
    is_avaiable = db.Column(db.Boolean,default=True)
    type = db.Column(db.String,nullable=False)
    desc = db.Column(db.String,nullable=True)
    menu_id = db.Column(db.Integer,db.ForeignKey('menu.id'),nullable=False)


    def __str__(self):
        return f'{self.name}'