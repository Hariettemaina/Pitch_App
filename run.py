from multiprocessing import Manager
from xmlrpc.client import Server
from app import create_app,db
from app.models import User
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = create_app('dev')

manager = Manager(app)
manager.add_command('sever', Server)

db = SQLAlchemy(app)
migrate = Migrate(app,db)



@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User)



if __name__ == '__main__':
    app.run()