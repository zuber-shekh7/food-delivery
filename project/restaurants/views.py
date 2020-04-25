from flask import Blueprint,render_template,url_for,redirect,flash,request
from flask_login import login_user,logout_user,current_user

from project.app import db
from .models import Restaurant

restaurants = Blueprint('restaurants',__name__,url_prefix='/restaurants/',template_folder='templates/')


@restaurants.route('/')
def index():
    restaurants = Restaurant.query.all()

    return render_template('restaurants/list.html',restaurants=restaurants)

@restaurants.route('/restaurant/<int:id>')
def view(id):
    restaurant = Restaurant.query.get_or_404(id)

    return render_template('restaurants/view.html',restaurant=restaurant)