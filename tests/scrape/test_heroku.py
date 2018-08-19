import unittest


def application(environ, start_response):
    headers = [('Content-Type', 'text/html; charset=utf8'),
               ('Content-Length', str(len(body)))]
    start_response('200 OK', headers)
    return [body]


def test_index(testapp):
    rv = testapp.get('/')
    assert rv.status == "200 OK"


def test_volcanoes(testapp):
    rv = testapp.get('/volcanoes')
    assert rv.status == "200 OK"


def test_comics(testapp):
    rv = testapp.get('/comics')
    assert rv.status == "200 OK"


def test_comics_api(testapp):
    rv = testapp.get('/comics/api/cbr')
    assert rv.status == "200 OK"


def test_comics_api_error(testapp):
    rv = testapp.get('/comics/api/crb')
    assert rv.status == "404 NOT FOUND"


if __name__ == '__main__':
    unittest.main()
