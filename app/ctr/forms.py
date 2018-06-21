from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('type your nickname',validators=[DataRequired()])
    userpass = StringField('type your password', validators=[DataRequired()])
    submit = SubmitField('Submit')