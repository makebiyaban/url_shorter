from flask import render_template
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
    
@app1.route('/login')
def login():
	form=LoginForm()
	return render_template('login.html',title='sign in',form=form)