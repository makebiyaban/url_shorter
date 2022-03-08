from crypt import methods
from flask import render_template, flash, redirect, url_for
from url_app import app1
from url_app.forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, login_required, logout_user
from url_app.models import User

@app1.route('/')
@app1.route('/index')
#@login_required
def index():
    user={'username':'mohammad'}
    posts=[
    {
        'author':{'username':'Ali'},
        'body':'this is great and im glad to programming'
    },
    {
        'author':{'username':'mehdi'},
        'body':'my instagram is dead!'
    },
    {'author':{'username':'amirmohammad'},
    'body':'my name is amir and i am bikar!'}
    ]
    return render_template('index.html',title='home page',user=user,posts=posts)
    
@app1.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():            
        user=User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid username or password')
            return redirect(url_for('login'))
        login_user(user,remember=form.remmber_me.data)
        return redirect(url_for('index'))
    return render_template('login.html',title='sign in',form=form)

@app1.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    return render_template('register.html',title='register new user',form=form)

@app1.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))