from flask import Blueprint,render_template,url_for,redirect,flash,request
from flask_login import login_user,logout_user,current_user
from project.app import db

from .forms import LoginForm,SignupForm
from .models import User

accounts = Blueprint('accounts',__name__,url_prefix='/accounts/',template_folder='templates/')


@accounts.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('logged in successfull')
            return redirect(url_for('accounts.home'))
        flash('invalida username or password')
        return redirect(url_for('accounts.login'))
    return render_template('accounts/login.html',form=form)


@accounts.route('/signup',methods=['GET','POST'])
def signup():
    form = SignupForm()
    form.type.data = request.args.get('type')
    if form.validate_on_submit():
        user = User(
            form.email.data,
            form.password.data,
            form.fname.data,
            form.lname.data,
            form.mobile.data,
            form.type.data,
        )
        db.session.add(user)    
        db.session.commit()
        flash('user created successfull')
        return redirect(url_for('accounts.login'))
    return render_template('accounts/signup.html',form=form,type=type)


@accounts.route('/home')
def home():
    if current_user.type == 'user':
        return render_template('accounts/home.html')
    elif current_user.type == 'restaurant':
        return render_template('accounts/user_restaurant.html')
    else:
        return render_template('accounts/user_delivery.html')


@accounts.route('/logout')
def logout():
    logout_user()
    flash('logged out successfull')
    return redirect(url_for('accounts.login'))