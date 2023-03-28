from run import app
import pytest, json


class TestAPI:

    def test_api_posts(self):
        response = app.test_client().get("/api/posts")
        json_data = response.get_json()

        assert response.status_code == 200
        assert type(json_data) is list
        for post in json_data:
            for key in ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]:
                assert key in post.keys()

    def test_api_post(self):
        response = app.test_client().get("/api/posts/1")
        post = json_data = response.get_json()

        assert response.status_code == 200
        assert type(json_data) is dict
        for key in ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]:
            assert key in post.keys()

