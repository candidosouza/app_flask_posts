from settings.settings import setting
from posts.index import posts


app = setting.app
app.register_blueprint(posts)


if __name__ == '__main__':
    app.run(debug=setting.env['DEBUG'])
    # app.run()

# @app.route('/', endpoint='index')
# def index():
#     return render_template('index.html')
#
#
# @app.errorhandler(404)
# def handler_error(error):
#     return render_template('404.html', error=error)
