''' Test and see if User and Post models are in default locations '''

def test_post_model():
    try:
        from app.Post import Post
        assert True
    except ImportError:
        assert False, "Error importing Posts model"

def test_user_model():
    try:
        from app.User import User
        assert True
    except ImportError:
        assert False, "Error importing Posts model"