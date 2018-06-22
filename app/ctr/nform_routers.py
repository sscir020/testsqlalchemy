from flask import render_template,url_for,redirect,flash,session
from ..models import Opr,Material,User
from . import ctr



@ctr.route('/')
@ctr.route('/welcome')
def welcome_user():
    # return "welcome_user"
    return render_template('welcome.html')


@ctr.route('/material_list')
def show_materials():
    if session['userid']!=None:
        return render_template('material_table.html',materials=Material.query.all())
    return url_for('ctr.log_user_in')


#
# @ctr.route('/logout')
# def log_user_out():
#     if session['userid']!=None:
#         session.pop('userid',None)
#         session.pop('username', None)
#         flash("You logged out")
#         return render_template('welcome.html')
