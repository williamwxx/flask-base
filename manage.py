import os
from flask.ext.script import Manager, Shell
from app import create_app,db
from app.models import News
from flask_migrate import Migrate, MigrateCommand,upgrade
from flask import Flask


app = create_app('production')
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app, db=db,News=News)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=False)

@manager.command
def forged():
    from forgery_py import basic, lorem_ipsum, name, internet, date
    from random import randint
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()
