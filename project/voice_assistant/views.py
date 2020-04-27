import os
from flask import Blueprint,render_template,url_for,redirect,flash,request,session
from flask_login import current_user,login_required
from project.config import Config

voice = Blueprint('voice',__name__,url_prefix='/voice',template_folder='templates/')

CONVERSATION_DIR = os.path.join(Config.ASSEST_DIR,'conversations')


@voice.route('')
@login_required
def index():
    filepath = os.path.join(CONVERSATION_DIR,f'{current_user.fname}.txt')

    if os.path.exists(filepath):
        with open(filepath,'r') as file:
            conversation = file.readlines()
            conversation = [tuple(i.split('-')) for i in conversation]
            session['conversation'] = conversation
    else:
        with open(os.path.join(filepath),'w') as file:
            pass

    return render_template('voice_assistant/index.html')


@voice.route('/recognize')
@login_required
def recognize():
    filepath = os.path.join(CONVERSATION_DIR,f'{current_user.fname}.txt')
    input = request.args.get('command')
    with open(os.path.join(filepath),'a') as file:
            file.write('user-'+input+'\n')
    return redirect(url_for('voice.index'))