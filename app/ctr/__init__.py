from flask import Blueprint

ctr=Blueprint('ctr',__name__)

from . import ctruser,errors,nform_routers,form_routers