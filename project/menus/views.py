from flask import Blueprint,render_template,url_for,redirect,flash,request
from flask_login import login_user,logout_user,current_user

from project.app import db


menus = Blueprint('menus',__name__,url_prefix='/menus/',template_folder='templates/')


@menus.route('/')
def index():
    return 'menus'