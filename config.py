import os

WTF_CSRF_ENABLED = True
SECRET_KEY = str(os.environ.get('SECRET_KEY'))

basedir = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Uploads
UPLOADS_DEFAULT_DEST = TOP_LEVEL_DIR + '/app/static/resources/'
UPLOADS_DEFAULT_URL = 'http://localhost:5000/static/resources/'

UPLOADED_IMAGES_DEST = TOP_LEVEL_DIR + '/app/static/resources/'
UPLOADED_IMAGES_URL = 'http://localhost:5000/static/resources/'

REGISTER_CODE = os.environ.get('SECRET_KEY_REGISTER')
