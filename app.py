from settings.settings import setting
from posts.index import posts


app = setting.app
app.register_blueprint(posts)

setting.db.create_all()


if __name__ == '__main__':
    app.run(debug=setting.env['DEBUG'])
    # app.run()

