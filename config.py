import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = 'pao-pao-d333-d-d-d-d-'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')