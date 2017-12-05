import os
from flask import Flask
#导入数据库模型，flask-admin对象用以初始化
from flask_admin import Admin
from Blog.data_model.models import Post,Comment,User,Tag,Diary
from Blog.background.admin_model import Flask_Blog_ModelView,Blog_view,Edit_view,Back_View,Edit_diary_view
#导入bcrypt对象用于初始化
from extension import bcrypt
#导入flask-login对象用于初始化
from flask_login import LoginManager
#导入蓝图api_views
from Blog.login.views import login_api
from Blog.main.views import main_api
from Blog.blog.views import blog_api
from Blog.diary.views import diary_api
from Blog.photos.views import photos_api
#上传导入
from flask_uploads import configure_uploads,patch_request_class
from Blog.photos.views import photos
#应用对象
app = Flask(__name__)
#配置文件配置
app.config.from_object('config')
#导入db对象
from extension import db
db.init_app(app)
@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()
#后台管理配置
admin = Admin(app,name=u'后台管理系统')
admin.add_view(Flask_Blog_ModelView(User,db.session))
admin.add_view(Blog_view(Post,db.session))
admin.add_view(Flask_Blog_ModelView(Comment,db.session))
admin.add_view(Flask_Blog_ModelView(Tag,db.session))
admin.add_view(Flask_Blog_ModelView(Diary,db.session))
admin.add_view(Edit_view(name=u'编辑博客'))
admin.add_view(Edit_diary_view(name=u'编辑日记'))
admin.add_view(Back_View(name=u'回到主页'))
#蓝图
app.register_blueprint(login_api,url_prefix='/login_register')
app.register_blueprint(main_api)
app.register_blueprint(blog_api,url_prefix='/blog')
app.register_blueprint(diary_api,url_prefix='/diary')
app.register_blueprint(photos_api,url_prefix='/photos')
#初始化bcrypt
bcrypt.init_app(app)
#初始化配饰login_manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login_api.login'
login_manager.login_message=u'请先登陆（暂时不开放注册）'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#上传配置
configure_uploads(app, photos)
patch_request_class(app)# set maximum file size, default is 16MB
#Ckeditor init
from Blog.flask_ckeditor import CKEditor
ckeditor = CKEditor(app)
#Moment时间模块
from extension import moment
moment.init_app(app)
#mail初始化
# from extension import mail
# mail.init_app(app)
