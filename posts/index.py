from flask import Blueprint

posts = Blueprint('posts', __name__)


@posts.route('/', methods=['GET'], endpoint='posts')
def main():
    return 'Posts routes'
