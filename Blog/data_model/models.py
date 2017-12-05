from flask_login import UserMixin
from extension import bcrypt
from extension import db

#用户
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(260))
    icon = db.Column(db.String(300))

    def __init__(self,name=None,email=None,password=None,**kwargs):
        super(User, self).__init__(**kwargs)
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % (self.name)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
#Blog文章
class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    short_body = db.Column(db.Text)
    body = db.Column(db.Text)
    time = db.Column(db.DateTime)
    u_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    user = db.relationship('User',backref=db.backref('posts'))
    blog_image = db.Column(db.String(300))
    t_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    tag = db.relationship('Tag', backref=db.backref('posts'))

    def __init__(self,title=None,short_body=None,body=None,time=None,user=None,blog_image=None,**kwargs):
        super(Post, self).__init__(**kwargs)
        self.title = title
        self.short_body=short_body
        self.body = body
        self.time=time
        self.user=user
        self.blog_image=blog_image

    def __repr__(self):
        return '<Post %r>' % (self.title)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    comment = db.Column(db.Text)
    p_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    post = db.relationship('Post', backref=db.backref('comments'))

    def __init__(self,name=None,email =None,comment=None,post=None,**kwargs):
        super(Comment, self).__init__(**kwargs)
        self.name=name
        self.email = email
        self.comment = comment
        self.post=post

    def __repr__(self):
        return '<Comments %r>' % (self.name)

class Tag(db.Model):
    __tablename__='tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),unique=True)

    def __repr__(self):
        return '<tags %r>' % (self.name)

class Diary(db.Model):
    __tablename__ = 'diarys'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    short_body = db.Column(db.String(300))
    body = db.Column(db.Text)
    time = db.Column(db.DateTime)
    diary_image = db.Column(db.String(300))
    u_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('diarys'))