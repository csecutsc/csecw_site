from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask.ext.bcrypt import Bcrypt
from .momentjs import momentjs

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
bcrypt = Bcrypt(app)

app.jinja_env.globals['momentjs'] = momentjs

from app import views, models
