
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime





class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    about = db.Column(db.String(255))
    avatar = db.Column(db.String())
    password_encrypt=db.Column(db.String(128))
    pitches = db.relationship('Pitches', backref='user', lazy='dynamic')
    likes = db.relationship('UpVote', backref='user', lazy='dynamic')
    comments = db.relationship('Comments', backref='comments', lazy='dynamic')

    
    
    def __repr__(self): 
        return f'User {self.username}'
    
    
class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    comment = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    