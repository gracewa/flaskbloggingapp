from flask import render_template,request,redirect,url_for,abort, flash
from flask_login import login_required, current_user
from flask_user import roles_required
from ..models import User, Blogpost, Comment, Role
from . import main
from .forms import UpdateProfile, ContactForm, PostForm,CommentForm
from .. import db, photos
import cloudinary
import cloudinary.uploader
from cloudinary.uploader import upload
import cloudinary.api
from cloudinary.utils import cloudinary_url
from ..requests import get_blogs


@main.route('/', methods = ['GET','POST'])
def index():
    title = 'Welcome to Blogging App'
    blogs = get_blogs()
    return render_template('main/index.html', title=title, blogs=blogs)

@main.route('/about', methods = ['GET'])
def about():
    title = 'About Us'
    return render_template('main/about.html', title=title)

@main.route('/post', methods = ['GET','POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        blogpost = Blogpost(title=form.title.data, subtitle=form.subtitle.data, author=form.author.data, content=form.content.data)
        db.session.add(blogpost)
        db.session.commit()
        return redirect(url_for('main.index'))
    title = 'Post a Blog'
    return render_template('main/post.html', title=title, form=form)

@main.route('/post/<int:blog_id>')
def view_post(blog_id):

    '''
    View blogpost page function that returns the post details page and its data
    '''
    posts = Blogpost.query.filter_by(id = blog_id)
    comments = Comment.query.filter_by(blog_id = blog_id)

    return render_template('main/viewpost.html',posts=posts,comments = comments)

@main.route('/post/<int:blog_id>/comment', methods = ['GET','POST'])
@login_required
def new_comment(blog_id):
    posts = Blogpost.query.filter_by(id=blog_id)
    post = posts[0]
    form = CommentForm()
    if form.validate_on_submit():

        comment = Comment(comment_title = form.title.data, comment = form.comment.data, comment_author = form.name.data, blog_id = blog_id, username = current_user)

        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('main.view_post',blog_id = post.id ))

    return render_template('main/comment.html', form=form, posts=posts)

@main.route('/post/<int:blog_id>/comment/<int:comment_id>/delete', methods = ['GET','POST'])
@login_required
def delete_comment(blog_id, comment_id):
    comment = Comment.query.filter_by(blog_id = blog_id, id=comment_id).first()
    if comment.username != current_user:
        db.session.delete(comment)
        db.session.commit()
        flash('Your comment has been deleted!', 'success')
    else:
        flash('You cannot delete that comment', 'success')
    return redirect(url_for('main.view_post', blog_id=blog_id))


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