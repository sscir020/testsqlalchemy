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


oprenumCH ={
    Oprenum.INITADD.name: '新入库',
    Oprenum.INBOUND.name: '入库',
    Oprenum.OUTBOUND.name: '出库',
    Oprenum.REWORKING.name: '返修中',
    Oprenum.RESTORE.name: '返修入库'
}

class Sensorname(Enum):
    P25 = 1
    P10 = 2
    TSP = 3
    NOISE = 4
    WINDSPEED = 5
    WINDDIRECTION = 6
    TEMP = 7
    PRESSURE = 8
    HUMIDITY = 9
    NEGOXYGEN = 10
    RAINFALL = 11
    ILLUM = 12
    CH2O = 13
    SO2 = 14
    NO2 = 15
    O3 = 16
    CO = 17
    CO2 = 18
    H2S = 19
    VOC = 20
    O2 = 21
    RADIATION = 22
    NH3 = 23
    SOILTEMP = 24
    SOILHUMIDITY = 25
    PHOTOSYNTHESIS = 26
    ULTRAVIOLETRAYS = 27


class Param(Enum):
    PARAM_EIGHT = 8
    PARAM_SEVEN = 7
    PARAM_FIVE = 5
    PARAM_THREE = 3
    PARAM_ZERO = -1

params = {
    Param.PARAM_EIGHT.name: [Sensorname.P25.name, Sensorname.P10.name, Sensorname.TSP.name, Sensorname.NOISE.name, Sensorname.WINDSPEED.name,
                             Sensorname.WINDDIRECTION.name, Sensorname.TEMP.name, Sensorname.PRESSURE.name],
    Param.PARAM_SEVEN.name: [Sensorname.P25.name, Sensorname.P10.name, Sensorname.TSP.name, Sensorname.NOISE.name, Sensorname.WINDSPEED.name,
                             Sensorname.WINDDIRECTION.name, Sensorname.TEMP.name],
    Param.PARAM_FIVE.name:  [Sensorname.P25.name, Sensorname.P10.name, Sensorname.TSP.name, Sensorname.NOISE.name, Sensorname.WINDSPEED.name],
    Param.PARAM_THREE.name: [Sensorname.P25.name, Sensorname.P10.name, Sensorname.TSP.name]
}
paramnums = {
    Param.PARAM_EIGHT.name: [1, 1, 1, 1, 1, 1, 1, 1],
    Param.PARAM_SEVEN.name: [1, 1, 1, 1, 1, 1, 1],
    Param.PARAM_FIVE.name:  [1, 1, 1, 1, 1],
    Param.PARAM_THREE.name: [1, 1, 1]
}




# oprenum = {
#     Oprenum.INITADD:'INITADD',
#     Oprenum.INBOUND:'INBOUND',
#     Oprenum.OUTBOUND:'OUTBOUND',
#     Oprenum.REWORKING:'REWORKING',
#     Oprenum.RESTORE:'RESTORE'
# }