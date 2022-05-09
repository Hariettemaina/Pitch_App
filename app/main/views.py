
from . import main_blueprint
from flask import render_template
from ..models import User, Pitches,Comments,UpVote
#from app import app

# Views
@main_blueprint.route('/')
def home():

    '''
    View root page function that returns the index page and its data
    '''
    # pitches=Pitches.query.all()
    # identification = Pitches.user_id
    # posted_by = User.query.filter_by(id=identification).first()
    # #user = User.query.filter_by(id=current_user.get_id()).first()

    # return render_template('pitches.html', pitches=pitches, posted_by=posted_by, user=UserList)
