import unittest
from app.models import User
from app import db

class UserTestCase(unittest.TestCase):
    def setUp(self):
        u=User(user_name='a',user_pass='1234')
        u.prt()
        db.session.add(u)
        db.commit()


    def test_user(self):
        u=User.query.filter_by(user_name="a").first()
        u.change_pass('5678')
        u.prt()

if __name__=='__main__':
    unittest.main()