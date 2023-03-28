import json

from app.posts.dao.posts_dao import PostsDAO
from flask import Blueprint, redirect, render_template

bookmark_blueprint = Blueprint("bookmark_blueprint", __name__, template_folder="templates")
post_dao = PostsDAO()

@bookmark_blueprint.route("/add/<int:postid>")
def add_bookmark_page(postid):
    with open("data/bookmarks.json", "r", encoding="utf-8") as file:
        all_marks = json.load(file)

    unique_marks = set(all_marks)
    unique_marks.add(postid)
    all_marks = list(unique_marks)

    with open("data/bookmarks.json", "w", encoding="utf-8") as file:
        json.dump(all_marks, file)
    return redirect("/", code=302)


@bookmark_blueprint.route("/remove/<int:postid>")
def remove_bookmark_page(postid):
    with open("data/bookmarks.json", "r", encoding="utf-8") as file:
        all_marks = json.load(file)

    unique_marks = set(all_marks)
    unique_marks.discard(postid)
    all_marks = list(unique_marks)

    with open("data/bookmarks.json", "w", encoding="utf-8") as file:
        json.dump(all_marks, file)
    return redirect("/", code=302)


@bookmark_blueprint.route("/")
def show_bookmarks():
    posts = []
    with open("data/bookmarks.json", "r", encoding="utf-8") as file:
        all_marks = json.load(file)
    for number in all_marks:
        post = post_dao.get_post_by_pk(number)
        posts.append(post)
    bookmark_counter = len(all_marks)
    return render_template("bookmarks.html", posts=posts, bookmark_counter=bookmark_counter)
