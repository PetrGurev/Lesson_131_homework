from flask import Blueprint, render_template
from .dao.users_dao import UsersDAO
from  ..posts.dao.posts_dao import PostsDAO

user_blueprint = Blueprint("user_blueprint", __name__, template_folder="templates")

users_dao = UsersDAO()
posts_dao = PostsDAO()

@user_blueprint.route("/users/<username>")
def user_page(username):
    posts = posts_dao.get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts, username=username)

