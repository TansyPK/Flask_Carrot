from flask import Blueprint,render_template,request
from flask_login import login_required
from Blog.data_model.models import Tag,Diary
diary_api = Blueprint('diary_api',__name__)

@diary_api.route('/')
@login_required
def diary_view():
    tag = Tag.query.all()
    page = request.args.get('page', 1, type=int)
    diary = Diary.query.paginate(page, 3, False)
    return render_template('main_templates/diary.html',tags=tag,diarys=diary)

@diary_api.route('/<post_id>')
@login_required
def post_view(post_id):
    tag = Tag.query.all()
    post = Diary.query.filter(Diary.id == post_id).first()
    return render_template('main_templates/diary_single_post.html',tags=tag,post=post)