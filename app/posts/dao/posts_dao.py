from pprint import pprint

import config
import json
from app.users.dao.users_dao import UsersDAO


class PostsDAO:

    def __init__(self):
        self.path = config.POSTS_PATH

    def load_data(self):
        with open(self.path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_posts_all(self):
        posts = self.load_data()
        return posts

    def get_posts_by_user(self, user_name):
        all_posts = self.get_posts_all()
        all_users = UsersDAO().get_all_users()
        sorted_posts = []
        if user_name not in all_users:
            raise ValueError("This user doesn't exist")
        for post in all_posts:
            if post["poster_name"] == user_name:
                sorted_posts.append(post)
        return sorted_posts

    def search_for_posts(self, query):
        sorted_posts = []
        all_posts = self.get_posts_all()
        for post in all_posts:
            if query in post['content']:
                sorted_posts.append(post)
        return sorted_posts

    def get_post_by_pk(self, pk):
        sorted_posts = []
        all_posts = self.get_posts_all()
        for post in all_posts:
            if pk == post['pk']:
                return post
