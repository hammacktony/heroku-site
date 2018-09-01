def test_comics_sources_repository_import():
    try:
        from app.repositories.ComicsSourcesRepository import ComicsSourcesRepository
        assert True
    except ImportError:
        assert False, "Error importing ComicsSourcesRepository repositories"