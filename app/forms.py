from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from .models import User, Lecture
from app import images


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(
        'Email is required to login')])
    password = PasswordField('password', validators=[DataRequired(
        'Password is required to login')])


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[
        DataRequired('Email is required to register')])
    password = PasswordField('password', validators=[DataRequired(
        'Password is required to register')])
    code = StringField('code', validators=[DataRequired(
        'The secret code is required to register')])


class LectureForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    date = DateField('date', format='%m/%d/%Y')


class LectureMaterialForm(FlaskForm):
    description = StringField('description', validators=[DataRequired()])
    material = StringField('material', validators=[DataRequired()])

    # Get all choices
    choices = []
    lectures = Lecture.query.all()
    for lecture in lectures:
        choices.append((str(lecture.id), lecture.title))

    lecture = SelectField('lecture', choices=choices,
                          validators=[DataRequired()])

    # Get all material types
    choices = [('file powerpoint outline icon', 'Powerpoint'), ('file pdf outline icon', 'PDF'),
               ('file text outline icon', 'Text'), ('github icon', 'GitHub')]
    material_type = SelectField(
        'material_type', choices=choices, validators=[DataRequired()])


class NewsForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    summary = StringField('summary', validators=[DataRequired()])
    date = DateField('date', format='%m/%d/%Y')

    news = TextAreaField('news')

    image = FileField('image', validators=[
                      FileAllowed(images, 'Images only!')])
