from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,EqualTo
class register_form(FlaskForm):
    username = StringField('username',validators=[DataRequired(message=u'用户名不能为空')])
    password = PasswordField('password',validators=[DataRequired(message=u'密码不能为空'),EqualTo('confirm',message=u'两次输入的密码不一致')])
    email = StringField('email',validators=[DataRequired(message=u'邮箱不能为空')])
    confirm = PasswordField('repeat')