from app.posts.dao.posts_dao import PostsDAO
from app.comments.dao.comments_dao import CommentsDAO
import pytest

@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO()
    return posts_dao_instance

@pytest.fixture()
def comments_dao():
    comments_dao_instance = CommentsDAO()
    return comments_dao_instance


class TestPostsDao:

    def test_get_posts_all(self, posts_dao):
        test_func = posts_dao.get_posts_all()
        assert type(test_func) == list, 'Returns not a list'
        assert len(test_func) > 0, "Returns empty list"

    def test_get_posts_by_user(self, posts_dao):
        test_func = posts_dao.get_posts_by_user
        with pytest.raises(ValueError):
            test_func("Petr")

    def test_get_comments_by_post_id(self, comments_dao):
        test_func = comments_dao.get_comments_by_post_id
        with pytest.raises(ValueError):
            test_func(34)

    def test_search_for_posts(self, posts_dao):
        test_func = posts_dao.search_for_posts
        assert test_func("123asd") == [], "Do not return empty list"

    def test_get_post_by_pk(self, posts_dao):
        test_func = posts_dao.get_post_by_pk
        assert type(test_func(2)) == dict, 'Returns not a dict'
        assert len(test_func(2)) == 7, 'Returns not 7 keys'

