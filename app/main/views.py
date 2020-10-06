from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required

from ..models import User, Blogpost
from . import main
from .forms import UpdateProfile, ContactForm, PostForm
from .. import db, photos
import cloudinary
import cloudinary.uploader
from cloudinary.uploader import upload
import cloudinary.api
from cloudinary.utils import cloudinary_url

@main.route('/', methods = ['GET','POST'])
def index():
    title = 'Welcome to Blogging App'
    blogs = Blogpost.query.all()
    return render_template('main/index.html', title=title, blogs=blogs)

@main.route('/about', methods = ['GET'])
def about():
    title = 'About Us'
    return render_template('main/about.html', title=title)

@main.route('/post', methods = ['GET','POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        blogpost = Blogpost(title=form.title.data, subtitle=form.subtitle.data, author=form.author.data, content=form.content.data)
        db.session.add(blogpost)
        db.session.commit()
    title = 'Post a Blog'
    return render_template('main/post.html', title=title, form=form)

@main.route('/contact', methods = ['GET'])
def contact():
    title = 'Contact Us'
    form = ContactForm()
    return render_template('main/contact.html', title=title, form=form)


@main.route('/user/<uname>', methods = ['GET','POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

    return render_template("profile/profile.html", user = user, form=form)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = request.files['photo']
        upload = cloudinary.uploader.upload(filename)
        path = upload.get('url')
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))