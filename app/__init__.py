from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

db=SQLAlchemy()
bootstrap=Bootstrap()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:testdb1@localhost:3306/testdb1?charset=utf8'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SECRET_KEY'] = 'hard to guess string'




    # from .ctr import ctr as ctr_blueprint
    # app.register_blueprint(ctr_blueprint)
    from app.ctr import ctr
    app.register_blueprint(ctr)
    # app.register_blueprint(ctr,url_prefix='/ctr')

    db.init_app(app)
    bootstrap.init_app(app)

    return app