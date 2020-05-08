from flask import Blueprint,render_template,url_for,redirect,flash,request
from flask_login import login_user,logout_user,current_user

from project.app import db
from .models import Item
from .forms import CreateItemForm

items = Blueprint('items',__name__,url_prefix='/items/',template_folder='templates/')


@items.route('/items/<int:id>')
def view(id):
    item = Item.query.get_or_404(id)
    return render_template('items/view.html',item=item)

@items.route('/<int:mid>/item/new',methods=['GET','POST'])
def new(mid):
    form = CreateItemForm()
    if form.validate_on_submit():
        item = Item(form.name.data,form.price.data,form.quantity.data,form.unit.data,form.type.data,form.description.data,form.is_avaliable.data,mid)
        db.session.add(item)
        db.session.commit()
        flash('item created')
        return redirect(url_for('items.view',id=item.id))
    return render_template('items/new.html',form=form)