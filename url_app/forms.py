from sys import maxsize
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
	username=StringField(label='Username',validators=[DataRequired()])
	password=PasswordField(label='Password', validators=[DataRequired()])
	remmber_me=BooleanField(label='Remmeber me')
	submit=SubmitField(label='Sign in')


class RegisterForm(FlaskForm):
	name = StringField(label='first name')
	family = StringField(label='last name')
	birthday = DateField(label='birthday')
	email = StringField(label='email',validators=[DataRequired(), Email()])
	mobile = StringField(label='mobile phone number', render_kw={'placeholder':'09xxxxxxxx'})
	username = StringField(label='username',validators=[DataRequired()])
	password = StringField(label='password',validators=[DataRequired(),Length(min=8,max=32)])
	password2 = StringField(label='password',validators=[DataRequired(),EqualTo('password')])
	website = StringField(label='site or sosialnetwork')
	submit=SubmitField(label='sign up')
