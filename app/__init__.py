# coding: utf-8


from os import path
from flask import Flask,request,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

basedir = path.abspath(path.dirname(__file__))
db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    bootstrap.init_app(app)
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    @app.template_test('current_link')
    def is_current_link(link):
        return link == request.path
    return app


