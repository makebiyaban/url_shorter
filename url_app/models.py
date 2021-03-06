from datetime import datetime
from enum import unique
import imp
from xml.dom.pulldom import default_bufsize
from url_app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from url_app import login


class User (UserMixin, db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(32))
    family = db.Column(db.String(64))
    birthday = db.column(db.Date())
    mobile=db.Column(db.String(16),index=True, unique=True)
    website=db.Column(db.String(64))
    username=db.Column(db.String(64),index=True,unique=True)
    email=db.Column(db.String(120),index=True,unique=True)
    password_hash=db.Column(db.String(128))
    posts=db.relationship('Post',backref='author',lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    body=db.Column(db.String(140))
    timestamp=db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<post {}>'.format(self.body)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))