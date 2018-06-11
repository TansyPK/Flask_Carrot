from flask_login import current_user,login_required
from flask import redirect,url_for,request,flash,render_template
from Blog.web_forms.blog_form import blog_form
from flask_admin.contrib.sqla import ModelView
from Blog.data_model.models import Post,Diary
from flask_admin import expose,BaseView
from extension import db
from datetime import datetime
class Flask_Blog_ModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login_api.login', next=request.url))

class Blog_view(Flask_Blog_ModelView):
    can_create = False

class Edit_view(BaseView):
    @expose('/',methods=['GET','POST'])
    def index(self):
        current_time = datetime.now()
        form = blog_form()
        if form.validate_on_submit():
            post = Post(title=form.title.data,short_body=form.short_body.data,body=form.body.data,time=form.time.data,user=current_user)
            db.session.add(post)
            db.session.commit()
            flash(message=u'提交成功')
            return redirect(url_for('admin.index'))
        return render_template('edit_templates/edit.html', form=form,current_time=current_time)

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login_api.login', next=request.url))

class Back_View(BaseView):
    @expose('/')
    def index(self):
        return redirect(url_for('main_api.main_view'))

class Edit_diary_view(BaseView):
    @expose('/',methods=['GET','POST'])
    def index(self):
        current_time = datetime.now()
        form = blog_form()
        if form.validate_on_submit():
            post = Diary(title=form.title.data,short_body=form.short_body.data,body=form.body.data,time=form.time.data,user=current_user)
            db.session.add(post)
            db.session.commit()
            flash(message=u'提交成功')
            return redirect(url_for('admin.index'))
        return render_template('edit_templates/edit.html', form=form,current_time=current_time)

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login_api.login', next=request.url))