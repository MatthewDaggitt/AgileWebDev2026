import os

basedir = os.path.abspath(os.path.dirname(__file__))
default_db_path = 'sqlite:///' + os.path.join(basedir, 'myapp.db')

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('MYAPP_DATABASE_URL') or default_db_path
    SECRET_KEY = os.environ.get('MYAPP_SECRET_KEY')