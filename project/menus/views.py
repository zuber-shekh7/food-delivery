from flask import Blueprint,render_template,url_for,redirect,flash,request
from flask_login import login_user,logout_user,current_user

from project.app import db
from .models import Menu

menus = Blueprint('menus',__name__,url_prefix='/menus/',template_folder='templates/')


# @menus.route('/<int:id>')
# def index(id):
#     menus = Menu.query.filter_by(restaurant_id=id).all()
#     return render_template('menus/list.html',menus=menus)

@menus.route('/menu/<int:id>')
def view(id):
    menu = Menu.query.get_or_404(id)
    return render_template('menus/view.html',menu=menu)