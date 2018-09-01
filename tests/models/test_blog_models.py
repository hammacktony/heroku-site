def test_posts_model():
    try:
        from app.models.Post import Post
        assert True
    except ImportError:
        assert False, "Error importing Posts model"
