''' A Module Description '''
# from masonite.facades.Auth import Auth

from mods.scrape.search_criterion import criterion
from mods.scrape.sources import sources
from app.models import (
    BleedingCool,
    Cbr,
    ComicBook,
    ComicsBeat,
    Ign,
    Nerdist,
    Newsarama,
    Outhousers
)

class ComicsController:
    ''' Controller for Comic News Template'''

    def __init__(self):
        pass

    def show(self, Application, Request):
        ''' Show Comic News Template '''

        # retrieves data for each Model in the repository
        data = {
            'app': Application,
            "criterion": criterion,
            "bleedingcool": BleedingCool.select('title', 'link').get(),
            "cbr": Cbr.select('title', 'link').get(),
            "comicbook": ComicBook.select('title', 'link').get(),
            "comicsbeat": ComicsBeat.select('title', 'link').get(),
            "ign": Ign.select('title', 'link').get(),
            "nerdist": Nerdist.select('title', 'link').get(),
            "newsarama": Newsarama.select('title', 'link').get(),
            "outhousers": Outhousers.select('title', 'link').get()
        }
        return view('comics/news', data)