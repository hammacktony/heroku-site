import pytest

from wsgi import application
from webtest import TestApp as _TestApp


@pytest.mark.webtest
class TestRoutes(object):

    def setup_method(self):
        self.app = _TestApp(application)

    # Main Pages
    def test_index(self):
        resp = self.app.get('/')
        assert resp.status_int == 200

    def test_contact(self):
        resp = self.app.get('/contact')
        assert resp.status_int == 200

    def test_projects(self):
        resp = self.app.get('/projects')
        assert resp.status_int == 200

    def test_volcanoes(self):
        resp = self.app.get('/volcanoes')
        assert resp.status_int == 200

    def test_comics(self):
        resp = self.app.get('/comics')
        assert resp.status_int == 200

    # Blog pages
    def test_blog_main(self):
        resp = self.app.get('/blog')
        assert resp.status_int == 200

    def test_blog_post(self):
        resp = self.app.get('/blog/post/first-post')
        assert resp.status_int == 200

    def test_blog_category(self):
        resp = self.app.get('/blog/category/masonite')
        assert resp.status_int == 200

    def test_blog_author(self):
        resp = self.app.get('/blog/author/tonus')
        assert resp.status_int == 200
