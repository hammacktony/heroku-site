import unittest

from site.mods.scrape.data import get_data


class GetDataTestCase(unittest.TestCase):

    def test_get_data(self):
        # Production environment
        env = "Production"
        # Table
        table = "cbr"
        self.assertTrue(get_data(table, env) is not False)

    def test_wrong_environment(self):
        # Production environment
        env = "Productin"
        # Table
        table = "cbr"
        error_message = "You have selected an incorrect environment."
        with self.assertRaises(Exception) as context:
            get_data(table, env)
        self.assertTrue(f'{error_message}' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
