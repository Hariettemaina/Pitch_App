from . import main_blueprint
from flask import render_template
#from app import app

# Views
@main_blueprint.route('/')
def home():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Hello World'
    return render_template('index.html',message = message)