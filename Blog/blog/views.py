from flask import Blueprint,render_template,flash,redirect,url_for,request
from Blog.data_model.models import Post,Comment,Tag
from Blog.web_forms.comment_form import comment_form
from extension import db

blog_api = Blueprint('blog_api',__name__)
@blog_api.route('/<tag_id>')
def blog_view(tag_id):
    tag = Tag.query.all()
    page = request.args.get('page',1,type=int)
    if(tag_id == '0'):
        post = Post.query.paginate(page,3,False)
    else:
        post = Post.query.filter(Post.t_id == tag_id).paginate(page,3,False)
    return render_template('main_templates/blog.html',posts=post,tags=tag,current_tagid=tag_id)

@blog_api.route('/post/<post_id>',methods=['GET','POST'])
def post_view(post_id):
    tag = Tag.query.all()
    form = comment_form()
    post = Post.query.filter(Post.id == post_id).first()
    if form.validate_on_submit():
        comment = Comment(name=form.name.data,email=form.email.data,comment=form.comment.data,post=post)
        db.session.add(comment)
        db.session.commit()
        # flash(message=u'提交成功')
        return redirect(url_for('blog_api.post_view',post_id=post_id))
    return render_template('main_templates/single-post.html',post=post,form=form,tags=tag)