# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin import Admin

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
Migrate(app,db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
admin = Admin(app,name='adminapp')

####################################################################################

from project.accounts.views import accounts
from project.main.views import main
from project.restaurants.views import restaurants
from project.menus.views import menus
from project.items.views import items
from project.voice_assistant.views import voice


app.register_blueprint(accounts)
app.register_blueprint(main)
app.register_blueprint(restaurants)
app.register_blueprint(menus)
app.register_blueprint(items)
app.register_blueprint(voice)


from project.accounts import views
from project.main import views
from project.restaurants import views
from project.admin import views
from project.menus import views
from project.items import views
from project.voice_assistant import views

####################################################################################


####################################################################################
