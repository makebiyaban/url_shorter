from app1 import db

class User (db.Model):
    id=db.column(db.integer, primary_key=True)
    username=db.column(db.string(64),index=True,unique=True)
    email=db.column(db.string(120),index=True,unique=True)
    password_hash=db.column(db.string(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
