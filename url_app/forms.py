from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username=StringField(label='Username',validators=[DataRequired()])
	password=PasswordField(label='Password', validators=[DataRequired()])
	remmber_me=BooleanField(label='Remmeber me')
	submit=SubmitField(label='Sign in')