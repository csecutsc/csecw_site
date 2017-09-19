from flask import render_template, redirect, flash, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, bcrypt, images
from .forms import LoginForm, RegisterForm, LectureForm, LectureMaterialForm, NewsForm, ResourcesForm
from .models import User, Lecture, LectureMaterial, News, Resources
from config import REGISTER_CODE
import datetime


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/index')
def index():
    lectures = Lecture.query.all()
    materials = LectureMaterial.query.all()
    all_news = News.query.all()
    resources = Resources.query.all()

    return render_template('index.html', lectures=lectures,
                           materials=materials, all_news=all_news,
                           resources=resources)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = RegisterForm()

    if form.validate_on_submit():
        # Try to find user
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            flash("This account already exists.")
        else:
            # User does not exist so we check if code is correct
            if form.code.data == REGISTER_CODE:
                password = bcrypt.generate_password_hash(form.password.data)
                user = User(email=form.email.data, password=password)

                db.session.add(user)
                db.session.commit()

                flash("User has been registered")
                return redirect(url_for('login'))
            else:
                flash("The code is incorrect")
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            password_check = bcrypt.check_password_hash(
                user.password, form.password.data)

            if password_check:
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for('dashboard'))
            else:
                flash("The user and password do not match")
        else:
            flash("User does not exist in the database")
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False

    db.session.add(user)
    db.session.commit()
    logout_user()

    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def dashboard():
    news_form = NewsForm()
    lecture_form = LectureForm()
    material_form = LectureMaterialForm()
    resource_form = ResourcesForm()

    lectures = Lecture.query.all()
    materials = LectureMaterial.query.all()
    all_news = News.query.all()
    users = User.query.all()
    resources = Resources.query.all()

    return render_template("dashboard.html", title='Dashboard', lectures=lectures,
                           all_news=all_news, materials=materials, material_form=material_form,
                           news_form=news_form, lecture_form=lecture_form, users=users,
                           resources=resources, resource_form=resource_form)


@app.route('/dashboard/news', methods=['POST'])
@login_required
def news():
    form = NewsForm()

    if form.validate_on_submit():
        # Check if the news will have a modal or not
        modal = False
        if (form.news.data != None) and (form.news.data != ''):
            modal = True

        # Get formatted date
        formatted_date = datetime.datetime.strptime(
            str(form.date.data), '%Y-%m-%d').date()
        formatted_date = formatted_date + datetime.timedelta(days=1)

        # Get image details
        no_image = False
        try:
            filename = images.save(request.files['image'])
        except:
            filename = "No file"
            no_image = True

        if not no_image:
            url = '/static/resources/' + filename
        else:
            url = "None"

        news = News(title=form.title.data, date=formatted_date,
                    summary=form.summary.data, news=form.news.data,
                    modal=modal, filename=filename, url=url)
        db.session.add(news)
        db.session.commit()

        flash("News was added")
        return redirect(url_for('dashboard'))
    return render_template('add_news.html', title="Add news", form=form)


@app.route('/dashboard/lectures', methods=['POST'])
@login_required
def lectures():
    form = LectureForm()

    if form.validate_on_submit():
        # Get formatted date
        formatted_date = datetime.datetime.strptime(
            str(form.date.data), '%Y-%m-%d').date()
        formatted_date = formatted_date + datetime.timedelta(days=1)

        lecture = Lecture(title=form.title.data, date=formatted_date)
        db.session.add(lecture)
        db.session.commit()

        flash('New lecture was added')
        return redirect(url_for('dashboard'))

    return render_template('add_lecture.html', title="Add lecture", form=form)


@app.route('/dashboard/lectures/material', methods=['POST'])
@login_required
def material():
    form = LectureMaterialForm()

    if form.validate_on_submit():
        # Get the lecture for which this material is for
        lecture = Lecture.query.filter_by(id=form.lecture.data).first()

        lecture_material = LectureMaterial(description=form.description.data,
                                           url=form.material.data, lecture=lecture,
                                           icon=form.material_type.data)
        db.session.add(lecture_material)
        db.session.commit()

        flash('New lecture material was added')
        return redirect(url_for('dashboard'))

    return render_template('add_lecture_material.html', title="Add lecture material", form=form)


@app.route('/dashboard/resources', methods=['POST'])
@login_required
def resources():
    form = ResourcesForm()

    if form.validate_on_submit():
        resource = Resources(description=form.description.data,
                             url=form.resource.data, icon=form.resource_type.data)
        db.session.add(resource)
        db.session.commit()
        flash("New resource has been added")
        return redirect(url_for('dashboard'))


# Routes to delete items
# Delete lectures
@app.route('/dashboard/lectures/delete/<id>')
@login_required
def delete_lecture(id):
    lecture = Lecture.query.get(id)

    if (lecture is None):
        flash('Lecture is not found')
    else:
        db.session.delete(lecture)
        db.session.commit()
        flash('The lecture has been deleted.')
        return redirect(url_for('dashboard'))


# Delete lecture material
@app.route('/dashboard/lectures/material/delete/<id>')
@login_required
def delete_material(id):
    lecture_material = LectureMaterial.query.get(id)

    if (lecture_material is None):
        flash('Specified lecture material is not found')
    else:
        db.session.delete(lecture_material)
        db.session.commit()
        flash('The lecture material specified has been deleted.')
        return redirect(url_for('dashboard'))


# Delete resources
@app.route('/dashboard/lectures/resources/delete/<id>')
@login_required
def delete_resource(id):
    resource = Resources.query.get(id)

    if (resource is None):
        flash('Specified resource is not found')
    else:
        db.session.delete(resource)
        db.session.commit()
        flash('The resource specified has been deleted.')
        return redirect(url_for('dashboard'))


# Delete news
@app.route('/dashboard/news/delete/<id>')
@login_required
def delete_news(id):
    news = News.query.get(id)

    if (news is None):
        flash('Specified news item is not found')
    else:
        db.session.delete(news)
        db.session.commit()
        flash('The news item specified has been deleted.')
        return redirect(url_for('dashboard'))


# Delete user
@app.route('/dashboard/users/delete/<id>')
@login_required
def delete_user(id):
    user = User.query.get(id)

    if (user is None):
        flash('Specified user is not found')
    else:
        db.session.delete(user)
        db.session.commit()
        flash('The user specified has been deleted')
        return redirect(url_for('dashboard'))
