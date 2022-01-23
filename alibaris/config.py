import os 
class Config(object):
    SECRET_KEY =  os.getenv("SECRET_KEY") or "You know nothing John Snow!"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    