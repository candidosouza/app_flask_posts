from flask import Blueprint, render_template
from models.posts import Post

posts = Blueprint('post', __name__)


@posts.route('/', methods=['GET'])
def new():
    return "rendered posts"


@posts.errorhandler(404)
def handler_error(error):
    return "Error 404"
