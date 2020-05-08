from flask import Blueprint,render_template,url_for,redirect,flash,request,session
from flask_login import current_user

from project.app import db
from project.items.models import Item

cart = Blueprint('cart',__name__,url_prefix='/cart/',template_folder='templates/')


@cart.route('/')
def index():
    return render_template('cart/index.html')

@cart.route('/<int:id>')
def add(id):
    item = Item.query.get_or_404(id)
    if 'cart' not in session:
        session['cart']={}
        session['restaurant']=None
        
    if session['restaurant'] and session['restaurant']!=item.menu.restaurant.id:
        session['cart'].clear()
    
    if item.name in session['cart'].keys():
        session['cart'][item.name]['quantity'] += 1
        session['cart'][item.name]['price'] += item.price
    else:    
        session['cart'][item.name] = {
            'name': item.name,
            'price' : item.price,
            'quantity' : 1,
        }
        session['restaurant'] = item.menu.restaurant.id
    return redirect(url_for('cart.index'))


@cart.route('/empty')
def empty():
    if 'cart' in session:
        del session['cart']
        flash('cart emptied')
        return redirect(url_for('cart.index'))