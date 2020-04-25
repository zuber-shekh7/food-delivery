from flask import Blueprint,render_template,url_for,redirect,flash,request
from flask_login import login_user,logout_user,current_user

from project.app import db


items = Blueprint('items',__name__,url_prefix='/items/',template_folder='templates/')


@items.route('/')
def index():
    return 'items'