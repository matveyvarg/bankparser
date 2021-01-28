import csv
from typing import Iterable, Union

from pathlib import Path

from .utils import map_data


class AbstarctWriter:
    """
    Abstact Base Class for Unified output
    """

    def __init__(self, pathfile: Union[str, Path], data: Iterable, ouput_format: dict = None, ):

        self.data = data
        self.ouput_format = ouput_format
        self.pathfile = pathfile

        if ouput_format:
            self.data = self.format_output(ouput_format)

    def format_output(self, ouput_format: dict = None) -> Iterable:
        """
        Format wirter data to given output

        Args:
            ouput_format (dict, optional): Given format. Defaults to None.

        Returns:
            Iterable: [description]
        """
        raise NotImplementedError

    def save(
        self,
        data: Iterable = None,
    ):
        """
        Write data to file

        Args:
            data (Iterable, optional): [description]. Defaults to None.
        """
        raise NotImplementedError


class CSVWriter(AbstarctWriter):
    """
    CSV Writer
    """

    def __init__(
        self,
        pathfile: Union[str, Path],
        data: Iterable,
        write_header: bool = False,
        *args,
        **kwargs
    ):
        self.write_header = write_header
        super().__init__(pathfile, data, *args, **kwargs)

    def format_output(self):
        return self.data

    def save(self):
        """
        Write csv to file

        Args:
            pathfile (Union[str, Path]): [description]
        """
        data = self.format_output()
        with open(self.pathfile, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            if self.write_header:
                writer.writeheader()

            writer.writerows(data)
