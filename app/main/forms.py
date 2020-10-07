from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email
from ..models import User


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    subtitle = StringField('Subtitle', validators=[Required()])
    author = StringField('Your Name', validators=[Required()])
    content = StringField('Blog',validators =[Required()])
    submit = SubmitField('Submit Blog')

class ContactForm(FlaskForm):
    name = StringField('Your Name',validators=[Required()])
    email = StringField('Your Email Address',validators=[Required(),Email()])
    message = StringField('Your Message',validators =[Required()])
    submit = SubmitField('Send')

class CommentForm(FlaskForm):
    title = StringField('Comment Title',validators=[Required()])
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')