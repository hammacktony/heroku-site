''' A Module Description '''
from masonite.facades.Auth import Auth

from mods.scrape import search_criterion
from mods.scrape import sources
from app.repositories.ComicsSourcesRepository import ComicsSourcesRepository


class ComicsController:
    ''' Controller for Comic News Template'''

    def __init__(self):
        """Due to the amount of news sites, I set up a repository of the all the classes that will be need. 

        Initializes this repository.
        """
        self.repo = ComicsSourcesRepository()

    def show(self, Application, Request):
        ''' Show Comic News Template '''

        srcs = sources.sources  # Comic News Sources
        # retrieves data for each Model in the repository
        jobs = [self.repo.return_data(src) for src in srcs]
        data = {
            'app': Application,
            'Auth': Auth(Request),
            "criterion": search_criterion.criterion,
            "bleedingcool": jobs[0],
            "cbr": jobs[1],
            "comicbook": jobs[2],
            "comicsbeat": jobs[3],
            "ign": jobs[4],
            "nerdist": jobs[5],
            "newsarama": jobs[6],
            "outhousers": jobs[7]
        }
        return view('comics/news', data)