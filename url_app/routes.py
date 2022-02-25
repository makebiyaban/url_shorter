from lzma import FORMAT_AUTO
from flask import render_template, flash, redirect
from prompt_toolkit import formatted_text
from url_app import app1
from url_app.forms import LoginForm

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
    if form.validate_on_submit():
        flash('login requested for user {}, remmber_me={}'.format(form.username.data, form.remmber_me.data))
        return redirect('/')
    return render_template('login.html',title='sign in',form=form)