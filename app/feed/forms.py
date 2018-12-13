from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, PasswordField # BooleanField
from wtforms.validators import Required, Email, EqualTo


class LoginForm(FlaskForm):
    email = TextField('Email Address', [Email(),
                                        Required(message='Forgot your email address?')])
    password = PasswordField('Password',[
                             Required(message='Must provide a password. ;-)')])
    capcha = RecaptchaField()

class SignForm(FlaskForm):
    email = TextField('Username', [TextField(),
                                        Required(message='Forgot your email address?')])
    email = TextField('Email Address', [Email(),
                                        Required(message='Forgot your email address?')])
    password = PasswordField('Password',[
                             Required(message='Must provide a password. ;-)')])
    capcha = RecaptchaField()
