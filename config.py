import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_NUM_PER_PAGE = 4
    SESSION_PERMANENT = True
    SESSION_KEY_PREFIX='session'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:hard_guess@localhost:3306/testdb1?charset=utf8'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Aosien2016@120.76.207.142:3306/osen?charset=utf8'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Aosien2016@120.76.207.142:3306/osen?charset=utf8'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
from enum import Enum
class Oprenum(Enum):
    INITADD = 1
    INCREASE = 2
    DECREASE = 3

oprenum = {
    Oprenum.INITADD:'initadd',
    Oprenum.INCREASE:'increase',
    Oprenum.DECREASE:'decrease'
}
