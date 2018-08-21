''' A Module Description '''

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

    def show(self, Application):
        ''' Show Comic News Template '''

        srcs = sources.sources  # Comic News Sources
        jobs = [self.repo.return_data(src) for src in srcs] # retrieves data for each Model in the repository
        data = {
            'app': Application,
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
