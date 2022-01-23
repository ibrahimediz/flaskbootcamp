from flask import Flask
from config import Config
from flask_sqalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
#app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
