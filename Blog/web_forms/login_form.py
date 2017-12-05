from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(message=u'用户名不能为空')])
    password = PasswordField('password',validators=[DataRequired(message=u'密码不能为空')])
    remember_me = BooleanField('remember_me')