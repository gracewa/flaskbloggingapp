import urllib.request,json
from flask import render_template,request,redirect,abort, flash, current_app
from flask_restful import Resource, Api, url_for
from app.main import main

def get_blogs():
    '''
    Function that gets the json response to our url request
    '''
    api = Api
    base_url = request.url
    get_blogs_url = (base_url + 'api/posts/')
    with urllib.request.urlopen(get_blogs_url) as url:
        get_blogs_data = url.read()
        get_blogs_response = json.loads(get_blogs_data)

        blogs_results = None

        if get_blogs_response['result']:
            blog_results_list = get_blogs_response['result']


    return blog_results_list