from flask import Blueprint
from models.posts import Post

posts = Blueprint('posts', __name__)


@posts.route('/', methods=['GET'], endpoint='posts')
def main():
    return 'Posts routes'


# @app.errorhandler(404)
# def handler_error(error):
#     return render_template('404.html', error=error)
