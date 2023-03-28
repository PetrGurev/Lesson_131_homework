from flask import Flask
from app.posts.views import posts_blueprint
from app.users.views import user_blueprint
from app.api.views import api_blueprint
from app.bookmark.views import bookmark_blueprint

app = Flask(__name__)

app.register_blueprint(posts_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(api_blueprint, url_prefix="/api")
app.register_blueprint(bookmark_blueprint, url_prefix="/bookmarks")


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Страница не найдена (код 404)</h1>"


@app.errorhandler(500)
def server_error(e):
    return "<h1>Ошибка сервера (код 500)</h1>"


if __name__ == "__main__":
    app.run()
