from flask_wtf import FlaskForm
from wtforms import StringField,DateTimeField,SubmitField
from Blog.flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired
class blog_form(FlaskForm):
    title = StringField('title',validators=[DataRequired(message=u'标题不能为空')])
    time = DateTimeField('time',validators=[DataRequired(message=u'编辑时间不能为空')])
    short_body = StringField('short_body',validators=[DataRequired(message=u'简述不能为空')])
    blog_image = StringField('blog_image')
    body = CKEditorField('body')
    submit = SubmitField('submit')


