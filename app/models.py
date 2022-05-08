from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    
    def __repr__(self): 
        return f'User {self.username}'
    
    
class Comments(db.Model):
    __table__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    comment = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer), db.ForeignKey('user.id')
    