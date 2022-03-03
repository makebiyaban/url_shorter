from flask import render_template, flash, redirect, url_for
from url_app import app1
from url_app.forms import LoginForm
from flask_login import current_user, login_user
from url_app.models import User

@app1.route('/')
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
    if current_user.authenticated:
        return redirect(url_for('/'))
    if form.validate_on_submit():    
        username=form.username.data
        user=User.query.filter_by(username).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid username or password')
            return redirect(url_for('login'))
        login_user(user,remember=form.remmber_me.data)
        return redirect(url_for('/'))
    return render_template('login.html',title='sign in',form=form)