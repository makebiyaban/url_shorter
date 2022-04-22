from crypt import methods
import email
from flask import render_template, flash, redirect, url_for
from matplotlib.pyplot import title
from url_app import app1,db
from url_app.forms import LoginForm, RegisterForm, ProfileForm
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
    if form.validate_on_submit():
        name = form.name.data
        family = form.family.data
        birthday = form.birthday.data
        mobile = form.mobile.data
        website = form.website.data
        username= form.username.data
        email = form.email.data
        password=form.password.data
        user=User(name=name, family=family, birthday=birthday, mobile=mobile, website=website, username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('tooo movafagh shodi')
        return redirect(url_for('login'))        
    return render_template('register.html',title='register new user',form=form)

@app1.route('/profile')
@login_required
def profile():
    form=ProfileForm()
    if form.validate_on_submit():
        name = form.name.data
        family = form.family.data
        birthday = form.birthday.data
        mobile = form.mobile.data
        website = form.website.data
        username= form.username.data
        email = form.email.data
        password=form.password.data
        user=User(name=name, family=family, birthday=birthday, mobile=mobile, website=website, username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('tooo movafagh shodi')
    return render_template('profile.html', title='user profile',form=form)

@app1.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))