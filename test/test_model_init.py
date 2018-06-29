import unittest
from app.models import *
from app import create_app,db
from main_config import Sensorname,Oprenum,Param,params,paramnums
import datetime
class paramTestCase(unittest.TestCase):
    def test_add(self):
        brands={'brand3':Param.PARAM_THREE,'brand5':Param.PARAM_FIVE,'brand7':Param.PARAM_SEVEN}
        app = create_app('development')
        app.app_context().push()
        with  app.app_context():
            print('***********************')
            print(list(brands)[0])
            print(list(brands.values())[0].name)
            print('***********************')
            print(params[Param.PARAM_THREE.name])
            for item in params[Param.PARAM_THREE.name]:
                print(item)
            print(paramnums[Param.PARAM_THREE.name])
            for i in range(0,Param.PARAM_THREE.value):
                print(list(params[Param.PARAM_THREE.name])[i])
                print((params[Param.PARAM_THREE.name])[i])
                # print(params[paramnums.PARAM_THREE.name][i])
            # for i in range(1,28):
            #     m=Material(material_name=Sensorname(i).name,countnum=10,reworknum=0,paramtype=Param.PARAM_ZERO.name)
            #     db.session.add(m)
            # m=Material(material_name=list(brands)[0],countnum=5,reworknum=0,paramtype=list(brands.values())[0].name)
            # db.session.add(m)
            # m = Material(material_name=list(brands)[1], countnum=5, reworknum=0, paramtype=list(brands.values())[1].name)
            # db.session.add(m)
            # m = Material(material_name=list(brands)[2], countnum=5, reworknum=0, paramtype=list(brands.values())[2].name)
            # db.session.add(m)
            # db.session.commit()
            #
            # for i in range(1,4):
            #     o=Opr(user_id=i,diff='5',material_id=i+27,oprtype=Oprenum.INITADD.name,momentary=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            #     db.session.add(o)
            # db.session.commit()
