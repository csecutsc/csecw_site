from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id', db.Integer, primary_key=True)
    email = db.Column('email', db.String(
        120), nullable=False, unique=True, index=True)
    password = db.Column('password', db.String(120))
    authenticated = db.Column(db.Boolean, default=False)

    def get_email(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % (self.username)


class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('title', db.String(120), unique=True)
    date = db.Column('date', db.DateTime)
    materials = db.relationship(
        'LectureMaterial', backref='lecture', lazy='dynamic')

    def __repr__(self):
        return '<Lecture %r>' % (self.id)


class LectureMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column('description', db.String)
    url = db.Column('url', db.String)
    icon = db.Column('icon', db.String)
    lecture_id = db.Column(db.Integer, db.ForeignKey('lecture.id'))

    def __repr__(self):
        return '<id: {}, description: {}, lecture_id: {}>'.format(self.id, self.description, self.lecture_id)


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    summary = db.Column('summary', db.String)
    news = db.Column('news', db.String)

    modal = db.Column(db.Boolean, default=False)
    filename = db.Column('filename', db.String, default=None, nullable=True)
    url = db.Column('url', db.String, default=None, nullable=True)

    date = db.Column('date', db.DateTime)

    def __repr__(self):
        return '<News %r>' % (self.id)
