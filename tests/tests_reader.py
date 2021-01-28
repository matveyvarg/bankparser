import unittest

from pathlib import Path
from typing import Iterable

from csvunifier.reader import CSVReader, DATA_FIELDS, AbstarctReader

DATA_KEYS = sorted(['date', 'type', 'integer', 'float', 'from', 'to'])


class TestCSVReaderSuccess(unittest.TestCase):
    """
    This test case tests successfull way
    """

    def assert_method(self, reader: AbstarctReader):
        """
        Common method for testing
        """
        data = reader.read()
        print(data)
        self.assertIsInstance(data, Iterable)
        self.assertEqual(sorted(data[0].keys()), sorted(DATA_FIELDS.keys()))
        

    def test_reader_bank1(self):
        """
        Run reader for a 1st bank file, and check the output
        """
        correct_file = Path('tests/test_data/bank1.csv')
        reader = CSVReader(correct_file, fields_map={
            'date': 'timestamp',
        })
        self.assert_method(reader)

    def test_reader_bank2(self):
        """
        Run reader for a 1st bank file, and check the output
        """
        correct_file = Path('tests/test_data/bank2.csv')
        reader = CSVReader(correct_file, fields_map={
            'type': 'transaction',
            'amount': 'amounts'
        })
        self.assert_method(reader)

    def test_reader_bank3(self):
        """
        Run reader for a 3st bank file, and check the output
        """
        correct_file = Path('tests/test_data/bank3.csv')
        reader = CSVReader(correct_file, fields_map={
            'date': 'date_readable',
            'amount': ('euro', 'cents')
        })
        self.assert_method(reader)


if __name__ == '__main__':
    unittest.main()
