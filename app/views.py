from flask import render_template, redirect, flash, url_for
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, bcrypt
from .forms import LoginForm, RegisterForm, LectureForm
from .models import User, Lecture


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/index')
def index():
    lectures = Lecture.query.all()
    return render_template('index.html', lectures=lectures)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # Try to find user
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            flash("This account already exists.")
        else:
            # User does not exist so we check if code is correct
            if form.code.data == "lmao":
                password = bcrypt.generate_password_hash(form.password.data)
                user = User(email=form.email.data, password=password)

                db.session.add(user)
                db.session.commit()

                flash("User has been registered")
                return redirect(url_for('login'))
            else:
                flash("The code is incorrect.")
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            password_check = bcrypt.check_password_hash(
                user.password, form.password.data)
            print(password_check)
            if password_check:
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for('index'))
        else:
            flash("woah")
        # TODO: Add actual login thing
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
    return "Dashboard bois"


@app.route('/dashboard/lectures', methods=['GET', 'POST'])
@login_required
def lectures():
    form = LectureForm()

    if form.validate_on_submit():
        lecture = Lecture(title=form.title.data, date=form.date.data.strftime('%Y-%m-%d'))

        db.session.add(lecture)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_lecture.html', title="Add lecture", form=form)
