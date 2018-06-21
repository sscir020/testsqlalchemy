from .__init__ import db

class User(db.Model):
    __tablename__ = 'users'
    user_id=db.Column(db.Integer,nullable=False,primary_key=True)
    user_name=db.Column(db.String(64),nullable=False, unique=True, index=True)
    user_pass = db.Column(db.String(64),nullable=False)


    # def __init__(self,**kwargs):
    #     # self.user_name=username
    #     # self.user_pass=userpass
    #     super(User, self).__init__(**kwargs)
    # def __init__(self, **kwargs):
    #     super(User, self).__init__(**kwargs)

    def change_pass(self,newpass):
        self.user_pass=newpass
        db.session.add(self)
        db.commit()
    def prt(self):
        print(self.user_id+':'+self.user_name+':'+self.user_pass)
