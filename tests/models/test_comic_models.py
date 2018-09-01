def test_bleedingcool_model():
    try:
        from app.models.BleedingCool import BleedingCool
        assert True
    except ImportError:
        assert False, "Error importing BleedingCool model"


def test_cbr_model():
    try:
        from app.models.Cbr import Cbr
        assert True
    except ImportError:
        assert False, "Error importing CBR model"


def test_comicbook_model():
    try:
        from app.models.ComicBook import ComicBook
        assert True
    except ImportError:
        assert False, "Error importing ComicBook model"

def test_ign_model():
    try:
        from app.models.Ign import Ign
        assert True
    except ImportError:
        assert False, "Error importing Ign model"

def test_nerdist_model():
    try:
        from app.models.Nerdist import Nerdist
        assert True
    except ImportError:
        assert False, "Error importing Nerdist model"

def test_newsarama_model():
    try:
        from app.models.Newsarama import Newsarama
        assert True
    except ImportError:
        assert False, "Error importing Newsarama model"

def test_outhousers_model():
    try:
        from app.models.Outhousers import Outhousers
        assert True
    except ImportError:
        assert False, "Error importing Outhousers model"
