from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id', db.Integer, primary_key=True)
    email = db.Column('email', db.String(120), nullable=False, unique=True, index=True)
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
    title = db.Column('title', db.String(120))
    date = db.Column('date', db.String(120))

    def __repr__(self):
        return '<Lecture %r>' % (self.id)
