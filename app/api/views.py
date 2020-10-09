from . import api, controllers
from flask import request


@api.route('/', methods=['GET'])
def welcome():
    return controllers.welcome()

@api.route('/posts/', methods=['GET'])
def get_all_post():
    return controllers.get_all_post()


@api.route('/posts/<id>', methods=['GET'])
def get_post(id):
    return controllers.get_single_post(id)