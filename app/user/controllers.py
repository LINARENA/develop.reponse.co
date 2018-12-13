from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.user.forms import LoginForm
from app.user.models import User


mod_user = Blueprint('user', __name__, url_prefix='/user')


@mod_user.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify(form.password.data):
            session['nick'] = user.username
            session['email'] = user.email
            flash('Welcome %s' % user.username)
            return redirect(url_for('dashboard'))
        flash('Wrong email or password', 'error-message')
    return render_template('/user/signin.html', form=form)

@mod_user.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('The email is already in use. Please choose another')
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('The username is already in use. Please choose another')
        user = User(form.email.data, form.username.data, form.password.data)
    return render_template('/user/signup.html')
