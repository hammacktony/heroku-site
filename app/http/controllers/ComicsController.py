''' A Module Description '''

import gevent
from orator import DatabaseManager

# User imports
from mods.scrape.data import get_data
from mods.scrape import search_criterion
from mods.scrape import sources


class ComicsController:
    ''' Controller for Comic News Template'''

    def show(self, Application):
        ''' Show Comic News Template '''

        config = {
            'postgres': {
                'driver': 'postgres',
                'host': 'ec2-54-235-244-185.compute-1.amazonaws.com',
                'database': 'dfqefn9gk5dgnj',
                'user': 'pmnkiouizlkvpb',
                'password': 'e42ed49071fb7526e39693d62def04878ae1ae68058a1b3c6526eca0be120c64',
                'prefix': ''
            }
        }

        db = DatabaseManager(config)
        srcs = sources.sources
        jobs = [gevent.spawn(get_data, src, db) for src in srcs]
        gevent.joinall(jobs, timeout=2)
        data = {
            'app': Application,
            "criterion": search_criterion.criterion,
            "bleedingcool": jobs[0].value,
            "cbr": jobs[1].value,
            "comicbook": jobs[2].value,
            "comicsbeat": jobs[3].value,
            "ign": jobs[4].value,
            "nerdist": jobs[5].value,
            "newsarama": jobs[6].value,
            "outhousers": jobs[7].value
        }
        return view('comics/news', data)
