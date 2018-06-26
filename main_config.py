#coding:utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_NUM_PER_PAGE = 8
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
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Aosien2016@120.76.207.142:3306/inventory?charset=utf8'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Aosien2016@120.76.207.142:3306/inventory?charset=utf8'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
from enum import Enum
class Oprenum(Enum):
    INITADD = 1
    INBOUND = 2
    OUTBOUND = 3
    REWORK = 4
    DELIVERY =5

oprenum = {
    Oprenum.INITADD:'INITADD',
    Oprenum.INBOUND:'INBOUND',
    Oprenum.OUTBOUND:'OUTBOUND',
    Oprenum.REWORK:'REWORK',
    Oprenum.DELIVERY:'DELIVERY'
}

oprenumCH ={
    'INITADD': '新添加',
    'INBOUND': '入库',
    'OUTBOUND': '出库',
    'REWORK': '返修入库',
    'DELIVERY': '返修出库'
}