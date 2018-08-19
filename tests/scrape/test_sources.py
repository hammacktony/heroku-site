import unittest
from site.mods.scrape.sources import sources


class ScrapeTestCase(unittest.TestCase):

    def test_sources(self):
        self.assertEqual(type(sources), type(list()))


if __name__ == '__main__':
    unittest.main()
