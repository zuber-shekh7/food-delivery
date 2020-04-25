# config.py
import os

class Config():
    BASE_DIR = os.path.abspath(os.path.dirname(__name__))
    SECRET_KEY = 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR,'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False