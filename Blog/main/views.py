from flask import render_template,Blueprint,redirect,url_for,flash
# from Blog.web_forms.contact_form import contact_form
from Blog.data_model.models import Tag
# from flask_mail import Message
# from extension import mail
# from smtplib import SMTP_SSL
main_api = Blueprint('main_api',__name__)

@main_api.route('/',methods=['GET','POST'])
def main_view():
    tag = Tag.query.all()
    return render_template('main_templates/index.html',tags=tag)

# @main_api.route('/contact',methods=['GET','POST'])
# def contact():
#     form = contact_form()
#     tag = Tag.query.all()
#     if form.validate_on_submit():
#         msg = Message(subject=form.name.data,
#                       recipients=['402704088@qq.com'])
#         msg.html = form.email_body.data
#         mail.send(msg)
#         flash(message=u'成功发送邮件')
#         return redirect(url_for('main_api.main_view'))
#     return render_template('main_templates/contact.html',tags=tag,form=form)