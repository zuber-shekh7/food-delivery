from project.app import admin,db
from flask_admin.contrib.sqla import ModelView
from project.accounts.models import User
from project.restaurants.models import Restaurant


# admin.add_view(UserView(User,db.session))
admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Restaurant,db.session))
# admin.add_view(ModelView(Restaurant,db.session))
# admin.add_view(ModelView(UserAddress,db.session))
