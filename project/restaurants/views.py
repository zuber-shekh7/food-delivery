from flask import Blueprint,render_template,url_for,redirect,flash,request
from flask_login import login_user,logout_user,current_user

from project.app import db
from .models import Restaurant
from .forms import CreateRestaurantForm

restaurants = Blueprint('restaurants',__name__,url_prefix='/restaurants/',template_folder='templates/')


@restaurants.route('/')
def index():
    restaurants = Restaurant.query.all()

    return render_template('restaurants/list.html',restaurants=restaurants)

@restaurants.route('/restaurant/<int:id>')
def view(id):
    restaurant = Restaurant.query.get_or_404(id)

    return render_template('restaurants/view.html',restaurant=restaurant)

@restaurants.route('/restaurant/new/<int:uid>',methods=['GET','POST'])
def new(uid):
    form = CreateRestaurantForm()

    if form.validate_on_submit():
        restaurant = Restaurant(form.name.data,form.license.data,current_user.id)
        db.session.add(restaurant)
        db.session.commit()
        flash('restaurant created')
        return redirect(url_for('restaurants.view',id=restaurant.id))
    return render_template('restaurants/new.html',form=form)