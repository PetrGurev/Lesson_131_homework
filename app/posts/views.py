# -*- coding: utf8 -*
from flask import Blueprint, render_template, request
from app.posts.dao.posts_dao import PostsDAO
from app.comments.dao.comments_dao import CommentsDAO


posts_blueprint = Blueprint("posts_blueprint",
                            __name__,
                            template_folder="templates")
posts_dao = PostsDAO()
comments_dao = CommentsDAO()


def tag_creater(posts: list | dict):
    if type(posts) == list:
        for j in range(len(posts)):
            content_words = posts[j]["content"]
            posts[j]["content"] = find_tag(content_words)
        return posts
    else:
        content_words = posts["content"]
        posts["content"] = find_tag(content_words)
        return posts



def find_tag(statement):
    text_words = statement.split()
    for i in range(len(text_words)):
        if "#" in text_words[i]:
            new_word = text_words[i].split("#")[1]
            text_words[i] = f"<a href=\"/tag/{new_word}\">#{new_word}</a>"
    new_statement = " ".join(text_words)
    return new_statement
    print(new_statement)


@posts_blueprint.route("/")
def main_page():
    posts = posts_dao.get_posts_all()
    posts = tag_creater(posts)
    return render_template("index.html", posts=posts)


@posts_blueprint.route("/search")
def search_page():
    query = request.args["s"]
    posts = posts_dao.search_for_posts(query)
    posts = tag_creater(posts)
    total_number = len(posts)
    return render_template("search.html", posts=posts, total_number=total_number)


@posts_blueprint.route("/posts/<int:postid>")
def post_page(postid):
    post = posts_dao.get_post_by_pk(postid)
    post = tag_creater(post)
    comments = comments_dao.get_comments_by_post_id(postid)
    total_comments = len(comments)
    return render_template("post.html",
                           post=post,
                           total_comments=total_comments,
                           comments=comments)


@posts_blueprint.route("/tag/<tagname>")
def tag_page(tagname):
    posts = posts_dao.search_for_posts(f"#{tagname}")
    posts = tag_creater(posts)
    return render_template("tag.html", posts=posts)

def mini(text_words):
    text_words = text_words.split()
    for word in text_words:
        if "#" in word:
            word = word.split("#")[1]
            word = f"<a href=\"/tag/{word}\"#{word}</a>"
    new_text = " ".join(text_words)
    return new_text
