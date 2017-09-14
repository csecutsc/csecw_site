from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    code = StringField('code', validators=[DataRequired()])


class LectureForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    date = DateField('date', format='%m/%d/%Y')