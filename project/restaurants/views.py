from flask import Blueprint,render_template,url_for,redirect,flash,request
from flask_login import login_user,logout_user,current_user

from project.app import db


restaurants = Blueprint('restaurants',__name__,url_prefix='/restaurants/',template_folder='templates/')


@restaurants.route('/')
def index():
    return 'restaurants'