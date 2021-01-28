from typing import Iterable

from datetime import datetime

def map_data(data: Iterable, field_map: dict, join_by) -> Iterable:
    """
    Mapp data to given format

    Args:
        data (Iterable): [description]
        field_map (dict): [description]

    Returns:
        Iterable: [description]
    """
    mapped_data = []

    for row in data:
        mapped_row = {}
        for key, value in field_map.items():
            if not isinstance(value, str):
                try:
                    # Try parse date
                    mapped_row[key] = datetime.strptime(row[value[0]],value[1])
                except Exception:
                    # If we have slpitted field we should join it to one field
                    # Example: If field 'amount' shoud consist of fields 'euro' and 'cents'
                    mapped_row[key] = join_by.join([row[inner_key] for inner_key in value])
            else:
                try:
                    mapped_row[key] = datetime.strptime(row[key], value)
                except Exception:
                    mapped_row[key] = row.get(value)

        mapped_data.append(mapped_row)

    return mapped_data
