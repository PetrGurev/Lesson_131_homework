import json
import config
from app.posts.dao.posts_dao import PostsDAO


class CommentsDAO:

    def __init__(self):
        self.path = config.COMMENTS_PATH

    def load_data(self):
        with open(self.path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_users_pk(self):
        all_posts = PostsDAO().get_posts_all()
        unique_pk = set()
        for post in all_posts:
            unique_pk.add(post["pk"])
        return unique_pk

    def get_comments_by_post_id(self, post_id):
        sorted_comments = []
        all_comments = self.load_data()
        unique_pk = self.get_users_pk()
        if post_id not in unique_pk:
            raise ValueError("This post doesn't exist")

        for comment in all_comments:
            if comment["post_id"] == post_id:
                sorted_comments.append(comment)
        return sorted_comments
