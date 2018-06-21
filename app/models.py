from .__init__ import db

class User(db.Model):
    __tablename__ = 'users'
    user_id=db.Column(db.Integer,nullable=False,primary_key=True)
    user_name=db.Column(db.String(64),nullable=False, unique=True, index=True)
    user_pass = db.Column(db.String(64),nullable=False)
    # def __init__(self,user_name,user_pass):
    #     u=super(User,user_name,user_pass)
    #     db.session.add(u)
    #     db.commit()