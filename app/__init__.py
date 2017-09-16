from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask.ext.bcrypt import Bcrypt
from flask_moment import Moment
from flask_uploads import UploadSet, IMAGES, configure_uploads

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
bcrypt = Bcrypt(app)

moment = Moment(app)

# Configure file uploading via Flask-uploads
images = UploadSet('images', IMAGES)
configure_uploads(app, images)

from app import views, models
