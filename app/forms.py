from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.fields.html5 import DateField
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
    title = StringField('title', validators=[
                        DataRequired('Title is required for a lecture')])
    date = DateField('date', format='%Y-%m-%d',
                     validators=[DataRequired('Date is required for a lecture')])


class LectureMaterialForm(FlaskForm):
    description = StringField('description', validators=[DataRequired()])
    material = StringField('material', validators=[DataRequired()])
    lecture = StringField('lecture', validators=[DataRequired()])

    # Get all material types
    choices = [('file powerpoint outline icon', 'Powerpoint'), ('file pdf outline icon', 'PDF'),
               ('file text outline icon', 'Text'), ('github icon', 'GitHub')]
    material_type = SelectField(
        'material_type', choices=choices, validators=[DataRequired()])


class NewsForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    summary = StringField('summary', validators=[DataRequired()])
    date = DateField('date', format='%Y-%m-%d')

    news = TextAreaField('news')

    image = FileField('image', validators=[
                      FileAllowed(images, 'Images only!')])


class ResourcesForm(FlaskForm):
    description = StringField('description', validators=[DataRequired()])
    resource = StringField('resource', validators=[DataRequired()])

    # Get all material types
    choices = [('file powerpoint outline icon', 'Powerpoint'), ('file pdf outline icon', 'PDF'),
               ('file text outline icon', 'Text'), ('github icon', 'GitHub'),
               ('desktop icon', 'Desktop'), ('browser icon', 'Browser')]
    resource_type = SelectField(
        'resource_type', choices=choices, validators=[DataRequired()])
