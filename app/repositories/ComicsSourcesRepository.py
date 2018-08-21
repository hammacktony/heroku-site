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

class ComicsSourcesRepository(object):

    def __init__(self):

        # Initiate all the Models
        self.bleedingcool = BleedingCool.BleedingCool()
        self.cbr = Cbr.Cbr()
        self.comicbook = ComicBook.ComicBook()
        self.comicsbeat = ComicsBeat.ComicsBeat()
        self.ign = Ign.Ign()
        self.nerdist = Nerdist.Nerdist()
        self.newsarama = Newsarama.Newsarama()
        self.outhousers = Outhousers.Outhousers()

        # Get all of model data
        self.bleedingcool.data = self.bleedingcool.all()
        self.cbr.data = self.cbr.all()
        self.comicbook.data = self.comicbook.all()
        self.comicsbeat.data = self.comicsbeat.all()
        self.ign.data = self.ign.all()
        self.nerdist.data = self.nerdist.all()
        self.newsarama.data = self.newsarama.all()
        self.outhousers.data = self.outhousers.all()

    def _set_source(self, src: str):

        switcher = {
            'bleedingcool': self.bleedingcool.data,
            'cbr': self.cbr.data,
            'comicbook': self.comicbook.data,
            'comicsbeat': self.comicsbeat.data,
            'ign': self.ign.data,
            'nerdist': self.nerdist.data,
            'newsarama': self.newsarama.data,
            'outhousers': self.outhousers.data
        }
        return switcher.get(src)

    def return_data(self, src: str):
        rows = self._set_source(src)
        titles = list()
        links = list()
        for row in rows:
            titles.append(row.title)
            links.append(row.link)

        results = list(zip(titles,links))
        return results