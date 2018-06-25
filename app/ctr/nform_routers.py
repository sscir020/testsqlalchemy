from flask import render_template,url_for,redirect,flash,session,request,current_app
from flask_login import login_user,logout_user,login_required,current_user
from ..models import Opr,Material,User
from . import ctr
from ..__init__ import db
from ..decorators import loggedin_required


@ctr.route('/')
@ctr.route('/welcome')
def welcome_user():
    # return "welcome_user"
    return render_template('welcome.html')


@ctr.route('/materials_list')
@loggedin_required
def show_materials():
    # print(session)
    # if session.get['userid'] is not None:
    page = request.args.get('page',1,type=int)
    pagination = Material.query.order_by(Material.material_id.desc()).\
        paginate(page,per_page=current_app.config['FLASK_NUM_PER_PAGE'],error_out=False)
    materials=pagination.items
    print(pagination==None)
    return render_template('material_table.html',materials=materials,pagination=pagination )
    # return render_template('material_table.html',materials=Material.query.all())
    # return url_for('ctr.log_user_in')


@ctr.route('/join_oprs_list')
@loggedin_required
def show_join_oprs():
    # if session['userid']!=None:
    # sql1=db.session.query(Opr.opr_id,Opr.diff,User.user_name).join(User,User.user_id==Opr.user_id).all()
    sql = db.session.query(Opr.opr_id, Opr.diff, User.user_name,Material.material_name).join(User, User.user_id == Opr.user_id)\
        .join(Material,Material.material_id==Opr.material_id).order_by(Opr.opr_id.desc())
    page = request.args.get('page', 1, type=int)
    pagination = sql.paginate(page, per_page=current_app.config['FLASK_NUM_PER_PAGE'], error_out=False)
    join_oprs=pagination.items
    # print(sql[0])
    return render_template('join_oprs_table.html',join_oprs=join_oprs,pagination=pagination)
    # return url_for('ctr.log_user_in')

@ctr.route('/logout')
@loggedin_required
def log_user_out():
    # logout_user()
    # print(session)
    session.pop('userid',None)
    session.pop('username', None)
    session.pop('userpass', None)
    flash("You are logged out")
    return redirect(url_for('ctr.welcome_user'))

# def url_for_other_page(page):
#     args = request.view_args.copy()
#     args['page']=page
#     return url_for(request.endpoint, **args)
# app.jinja_env.globals['url_for_other_page']=url_for_other_page

