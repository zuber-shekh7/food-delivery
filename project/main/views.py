from flask import Blueprint,render_template,url_for,redirect,flash,request


main = Blueprint('main',__name__,url_prefix='/',template_folder='templates/')


@main.route('')
def index():
    return render_template('main/index.html')


@main.route('/about')
def about():
    return render_template('main/about_us.html')


@main.route('/contact')
def contact():
    return render_template('main/contact_us.html')
