from flask import render_template,url_for,redirect,flash,session
from ..models import Opr,Material,User
from . import ctr
from ..__init__ import db



@ctr.route('/')
@ctr.route('/welcome')
def welcome_user():
    # return "welcome_user"
    return render_template('welcome.html')


@ctr.route('/materials_list')
def show_materials():
    if session['userid']!=None:
        return render_template('material_table.html',materials=Material.query.all())
    return url_for('ctr.log_user_in')


@ctr.route('/join_oprs_list')
def show_join_oprs():
    if session['userid']!=None:
        sql1=db.session.query(Opr).outerjoin(User,User.user_id==Opr.user_id).all()
        print(sql1[0])
        return render_template('join_oprs_table.html',join_oprs=sql1)
    return url_for('ctr.log_user_in')

#
# @ctr.route('/logout')
# def log_user_out():
#     if session['userid']!=None:
#         session.pop('userid',None)
#         session.pop('username', None)
#         flash("You logged out")
#         return render_template('welcome.html')
