import json
import config


class UsersDAO:

    def __init__(self):
        self.path_comments = config.COMMENTS_PATH
        self.path_posts = config.POSTS_PATH

    def get_all_users(self):
        all_users = set()
        with open(self.path_posts, "r", encoding="utf-8") as file:
            posts_data = json.load(file)
        for post in posts_data:
            all_users.add(post["poster_name"])
        with open(self.path_comments, "r", encoding="utf-8") as file:
            comments_data = json.load(file)
        for comment in comments_data:
            all_users.add(comment["commenter_name"])
        return list(all_users)
