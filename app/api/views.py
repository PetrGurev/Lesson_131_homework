import json, logging
import config

from flask import Blueprint, jsonify
from ..posts.dao.posts_dao import PostsDAO

# logging.basicConfig(filename="api.log",
#                     level=logging.INFO,
#                     format='%(asctime)s [%(levelname)s] %(message)s')

api_blueprint = Blueprint("api_blueprint", __name__)


@api_blueprint.route("/posts")
def api_posts():
    inst = PostsDAO()
    posts = inst.get_posts_all()
    # logging.INFO("Запрос /api/posts")
    return jsonify(posts)


@api_blueprint.route("/posts/<int:post_id>")
def api_post(post_id):
    post = PostsDAO().get_post_by_pk(post_id)
    # logging.INFO(f"Запрос /api/posts/{post_id}")
    return jsonify(post)


