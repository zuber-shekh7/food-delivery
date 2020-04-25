from flask import Blueprint,render_template,url_for,redirect,flash,request
from flask_login import login_user,logout_user,current_user

from project.app import db
from .models import Item

items = Blueprint('items',__name__,url_prefix='/items/',template_folder='templates/')


@items.route('/items/<int:id>')
def view(id):
    item = Item.query.get_or_404(id)
    return render_template('items/view.html',item=item)