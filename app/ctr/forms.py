from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,EqualTo

class EditOprForm(FlaskForm):
    diff=IntegerField("填写增加或减少数量,例如 10 或者 -10",  validators=[DataRequired()])
    submit=SubmitField('出入库')

class EditReworkOprForm(FlaskForm):
    diff=IntegerField("填写增加或减少数量,例如 10 或者 -10",  validators=[DataRequired()])
    submit=SubmitField('返修出入库')

class AddOprForm(FlaskForm):
    materialname=StringField("填写材料/物品名",validators=[DataRequired()])
    countnum=IntegerField("填写数量",  validators=[DataRequired()])
    submit=SubmitField('添加')

class RegistrationForm(FlaskForm):
    username=StringField("用户名-英文",validators=[DataRequired()])
    userpass=PasswordField("密码",validators=[DataRequired(),EqualTo('userpass2',message='密码不一致')])
    userpass2 = PasswordField("确认密码", validators=[DataRequired()])
    submit = SubmitField('注册')

class LoginForm(FlaskForm):
    username = StringField('用户名-英文',validators=[DataRequired()])
    userpass = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('登录')

