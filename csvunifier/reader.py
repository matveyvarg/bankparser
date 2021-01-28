import csv
import logging

from typing import Union, Iterable
from pathlib import Path

from .utils import map_data

logger = logging.getLogger(__name__)

DATA_FIELDS = {
    'date': 'date',
    'type': 'type',
    'amount': 'amount',
    'from': 'from',
    'to': 'to'
}


class AbstarctReader:
    """
    Abstarct class for other readers
    """

    def __init__(self, path: Union[Path, str] = "", fields_map: dict = None, join_by="."):
        """
        Args:
            path (str, optional): Path to file. Defaults to "".
            fields_map (dict, optional):
                If we have custom fields, we shold pass mapp this fields.
                Defaults to None.
        """
        if fields_map is None:
            fields_map = {}

        self.fields_map = {**DATA_FIELDS, **fields_map}

        self.path = path
        self.join_by = join_by

    def parse_file(self, filename: Union[Path, str] = "") -> Iterable:
        """
        Parse file and return data
        """
        raise NotImplementedError

    def map_fields(self, data: Iterable) -> dict:
        """
        Map file's fields to user's

        Returns:
            dict: mapped fields
        """
        raise NotImplementedError

    def read(self) -> dict:
        """
        Read file and generate mapped data

        Returns:
            dict: mapped data
        """
        raise NotImplementedError


class DefaultReadBehaviourMixin(object):
    """
    Mixin with default behaviour for read method
    1. read file
    2. map the data
    """
    def read(self) -> dict:
        """
        Read file and generate mapped data

        Returns:
            dict: mapped data
        """
        readed_data = self.parse_file(self.path) if self.path else self.parse_file()
        return self.map_fields(readed_data)


class CSVReader(DefaultReadBehaviourMixin, AbstarctReader):
    """
    Read data from csv files
    """

    def parse_file(self, filename: Union[Path, str] = "") -> Iterable:
        """
        Parse csv file

        Args:
            filename (str, optional): [description]. Defaults to "".

        Returns:
            Iterable: iterable object with csv rows
        """
        if not filename:
            filename = self.path

        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            return [row for row in reader]

    def map_fields(self, data: Iterable) -> Iterable:
        """
        Map fields from csv to given
        It's unnecessary to map it this way, but giv us more flexebility
        Args:
            data (Iterable): Iterable object with csv rows

        Returns:
            Iterable: mapped data
        """
        return map_data(data, self.fields_map, self.join_by)
