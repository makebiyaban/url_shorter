from url_app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

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
	password = PasswordField(label='password',validators=[DataRequired(),Length(min=6,max=32)])
	password2 = PasswordField(label='password',validators=[DataRequired(),EqualTo('password')])
	website = StringField(label='site or sosial network')
	submit=SubmitField(label='sign up')

	def validate_username(self, username):
		user=User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('please enter diffrent username')

	def validate_email(self, email):		
		user=User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('please enter diffrent email address')

class ProfileForm(FlaskForm):
	name = StringField(label='first name')
	family = StringField(label='last name')
	birthday = DateField(label='birthday')
	email = StringField(label='email',validators=[DataRequired(), Email()])
	mobile = StringField(label='mobile phone number', render_kw={'placeholder':'09xxxxxxxx'})
	username = StringField(label='username',validators=[DataRequired()])
	password = PasswordField(label='password',validators=[DataRequired(),Length(min=6,max=32)])
	password2 = PasswordField(label='password',validators=[DataRequired(),EqualTo('password')])
	website = StringField(label='site or sosial network')
	submit=SubmitField(label='update')

	def validate_username(self, username):
		user=User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('please enter diffrent username')

	def validate_email(self, email):		
		user=User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('please enter diffrent email address')