from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
import datetime
from marshmallow import fields, Schema


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    blogposts = db.relationship('Blogpost', backref='users', lazy=True)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'

class Blogpost(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_posted = db.Column(db.DateTime)

    def __init__(self, data):
        self.title = data.get('title')
        self.subtitle = data.get('subtitle')
        self.author = data.get('author')
        self.content = data.get('content')
        self.user_id = data.get('user_id')
        self.date_posted = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_blogposts():
        return Blogpost.query.all()

    @staticmethod
    def get_one_blogpost(id):
        return Blogpost.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)
class BlogpostSchema(Schema):
  """
  Blogpost Schema
  """
  id = fields.Int(dump_only=True)
  title = fields.Str(required=True)
  subtitle = fields.Str(required=True)
  author = fields.Str(required=True)
  contents = fields.Str(required=True)
  user_id = fields.Int(required=True)
  date_posted = fields.DateTime(dump_only=True)

class Comment(db.Model):

    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment_title = db.Column(db.String)
    comment = db.Column(db.String)
    posted = db.Column(db.Time,default=datetime.datetime.utcnow())
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(blog_id=id).all()
        return comments