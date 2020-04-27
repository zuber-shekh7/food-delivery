from flask import Blueprint,render_template,url_for,redirect,flash,request


voice = Blueprint('voice',__name__,url_prefix='/voice',template_folder='templates/')


@voice.route('')
def index():
    return render_template('voice_assistant/index.html')

@voice.route('/recognize')
def recognize():
    return "got you"