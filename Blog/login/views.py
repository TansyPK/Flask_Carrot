from flask import Blueprint,render_template,flash,redirect,url_for,request
from Blog.web_forms.login_form import LoginForm
from Blog.web_forms.register_form import register_form
from Blog.data_model.models import User
from extension import db
from flask_login import login_user,logout_user,login_required
login_api = Blueprint('login_api',__name__)

@login_api.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user,boolean_user = isuser(form.username.data,form.password.data)
        if boolean_user:
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main_api.main_view'))
    return render_template('login_templates/login.html',form=form)

@login_api.route('/register',methods=['GET','POST'])
@login_required
def register():
    form = register_form()
    if form.validate_on_submit():
        user = User(form.username.data,form.email.data,form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(message=u'注册成功，请登录')
        return redirect(url_for('login_api.login'))
    return render_template('login_templates/sign-up.html',form=form)

@login_api.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_api.main_view'))

#判断是不是存在的用户
def isuser(username,password):
    user = User.query.filter(User.name==username).first()
    if user!=None:
        if user.check_password(password):
            return user,True
        else:
            flash(message=u'密码错误')
            return user,False
    else:
        flash(message=u'用户名不存在')
        return user,False