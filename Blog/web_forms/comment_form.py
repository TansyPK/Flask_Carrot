from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from Blog.flask_ckeditor import CKEditorField
class comment_form(FlaskForm):
    name = StringField('name',validators=[DataRequired(message=u'名字不能为空')])
    email = StringField('email',validators=[DataRequired(message=u'邮箱不能为空')])
    comment = CKEditorField('comment')