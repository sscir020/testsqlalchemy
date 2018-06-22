from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
bootstrap=Bootstrap()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:testdb1@localhost:3306/testdb1?charset=utf8'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SECRET_KEY'] = 'hard to guess string'
    db.init_app(app)
    bootstrap.init_app(app)

    from .ctr import ctr as ctr_blurprint
    app.register_blueprint(ctr_blurprint)


    return app