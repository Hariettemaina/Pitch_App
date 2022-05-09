from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()




def create_app(config_name):
    app = Flask(__name__)
    
    
    db = SQLAlchemy(app)
    migrate.init_app = Migrate(app,db)
    
    #set up
    app.config.from_object(config_options[config_name])
    
    #init
    bootstrap.init_app(app)
    db.init_app(app)
    
    #regi blueprints
    from .main import main_blueprint
    app.register_blueprint(main_blueprint)

    
    return app