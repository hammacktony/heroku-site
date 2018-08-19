import unittest
from site.mods.scrape.search_criterion import criterion


class CriterionTestCase(unittest.TestCase):

    def test_criterion(self):
        self.assertEqual(type(criterion), type(list()))


if __name__ == '__main__':
    unittest.main()