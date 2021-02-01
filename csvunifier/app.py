from typing import Iterable, Generator, Union
from pathlib import Path

from csvunifier.reader import AbstarctReader, CSVReader
from csvunifier.writer import AbstarctWriter, CSVWriter


class App:
    """
    Main application
    """

    def __init__(
        self,
        files: Iterable[tuple],
        reader_class=None,
        writer_class=None
    ):
        """
        Constructor for application class
        It accept Iterable object with files and field mappings
        [(filepath, {field_mappings})]
        Args:
            files (Iterable[tuple]): [description]
            reader_class ([type], optional): [description]. Defaults to None.
            writer_class ([type], optional): [description]. Defaults to None.
        """
        self.reader_class = reader_class
        self.writer_class = writer_class

        self.files = files

        readed_data = []

        for readed_file in self.readed_files():
            readed_data += readed_file

        writer = self.get_writer(readed_data)
        writer.save()

    def get_reader(self, file_: Union[str, Path]) -> AbstarctReader:
        if self.reader_class:
            return self.reader_class

        if file_.endswith('.csv'):
            return CSVReader
        else:
            return AbstarctReader

    def get_writer(self, data):
        if not self.writer_class:
            return CSVWriter('output.csv', data, True)

    def readed_files(self) -> Generator:
        for file_, field_map in self.files:
            reader = self.get_reader(file_)(file_, field_map)
            yield reader.read()


if __name__ == '__main__':
    app = App([
        ('tests/test_data/bank1.csv', {'date': ('timestamp', '%b %d %Y')}),
        (
            'tests/test_data/bank2.csv',
            {'date': '%d-%m-%Y','type': 'transaction', 'amount': 'amounts'}
        ),
        (
            'tests/test_data/bank3.csv',
            {'date': ('date_readable', '%d %b %Y'), 'amount': ('euro', 'cents')}
        )
    ])