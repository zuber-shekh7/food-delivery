from project.app import db,bcrypt,login_manager
# from project.menus.models import Menu


class Restaurant(db.Model):
    
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    license = db.Column(db.String,nullable=False)
    is_open = db.Column(db.Boolean,default=False)
    menus = db.relationship('Menu',backref='restaurant',lazy=True)
    owner_id = db.Column(db.Integer,db.ForeignKey('users.id'),unique=True)


    def __init__(self,name,license,owner_id):
        self.name = name
        self.license = license
        self.owner_id = owner_id

    def __str__(self):
        return f'{self.name}'

