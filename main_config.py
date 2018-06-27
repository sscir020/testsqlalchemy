#coding:utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1AR4bnTnLHZyHaKt'
    SQLALCHEMY_POOL_SIZE = 100
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_NUM_PER_PAGE = 10
#SESSION_TYPE= 'redis'
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
    REWORKING = 4
    RESTORE =5

oprenum = {
    Oprenum.INITADD:'INITADD',
    Oprenum.INBOUND:'INBOUND',
    Oprenum.OUTBOUND:'OUTBOUND',
    Oprenum.REWORKING:'REWORKING',
    Oprenum.RESTORE:'RESTORE'
}

oprenumCH ={
    'INITADD': '新入库',
    'INBOUND': '入库',
    'OUTBOUND': '出库',
    'REWORKING': '返修中',
    'RESTORE': '返修入库'
}