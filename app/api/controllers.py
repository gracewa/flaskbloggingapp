from flask import jsonify, make_response
from app.models import Blogpost
from .utilities import get_post_data, bad_request
from app import db

def welcome():
    """
    Welcome API
    :return: Response Json object
    """
    resp = dict(status="success", message="Welcome to blog app!!")
    return jsonify(resp)

def get_all_post():
    """
    Get the List of Blog Posts
    :return: Response Json object
    """
    results= []
    try:
        posts = Blogpost.query.all()
        for post in posts:
            results.append({
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'author': post.author,

            })

        resp = dict(status="success",
                    message="Succeeded to get the blog posts!!",
                    result=results,
                    count=len(
                        results))
        return jsonify(resp)

    except Exception as e:
        msg = f"Failed to get the blog posts, Error: {str(e)}"
        return make_response(jsonify({"ERROR": msg}))




def get_single_post(id):
    """
    Get post details
    :param id: post id
    :return: Post Json Response
    """
    try:
        post = Blogpost.query.get(id)
        if not post:
            return make_response(
                jsonify(
                    {"ERROR": str(f"Post not found for id {id}!!")}))

        data = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author,

        }
        return jsonify(data)

    except Exception as e:
        msg = f"Failed to get a blog post, Error: {str(e)}"
        return make_response(jsonify({"ERROR": msg}))