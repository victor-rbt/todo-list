from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    passwd = PasswordField('password', validators=[DataRequired()])

class RegisterForm(Form):
    name = StringField('name', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    passwd = PasswordField('password', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])

class AddTaskForm(Form):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
