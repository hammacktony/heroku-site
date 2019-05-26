''' A Module Description '''
# from masonite.facades.Auth import Auth

from app.models import (BleedingCool, Cbr, ComicBook, ComicsBeat, Ign, Nerdist,
                        Newsarama, Outhousers)
from lib.scrape.search_criterion import criterion
from lib.scrape.sources import sources
from masonite.view import View


class ComicsController:
    ''' Controller for Comic News Template'''

    def __init__(self):
        pass

    def show(self, view: View):
        ''' Show Comic News Template '''

        # retrieves data for each Model in the repository
        data = {
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
        return view.render('comics/news', data)
