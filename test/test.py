import unittest
from example import *

class TestAverageCsv(unittest.TestCase):

    def test_path_error(self):
        with self.assertRaises(Exception):
            get_file_list(path='')

    def zero_value(self):
        self.assertEqual(csv_average_reader(), {'close': 0.0, 'high': 0.0, 'low': 0.0, 'open': 0.0})

    def test_value(self):
        self.assertEqual(csv_average_reader(), {'close': 67.753, 'high': 68.863, 'low': 66.833, 'open': 68.096})


if __name__ == "__main__":
    unittest.main()

