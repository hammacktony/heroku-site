from wsgi import application
from webtest import TestApp as _TestApp


class TestRoutes(object):

    def setup_method(self):
        self.app = _TestApp(application)

    def test_index(self):
        resp = self.app.get('/')
        assert resp.status_int == 400

    