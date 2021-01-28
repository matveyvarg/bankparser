import unittest
import os

from csvunifier.writer import CSVWriter


class TestWriter(unittest.TestCase):
    """
    Test writer of application
    """

    def test_writer(self):

        writer = CSVWriter('output.csv', [
            {'date': '3 Oct 2020'}
        ], True)

        writer.write_to_file()

        assert os.path.isfile('output.csv')
        os.remove('output.csv')


if __name__ == '__main__':
    unittest.main()
