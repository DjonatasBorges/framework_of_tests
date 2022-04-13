from typing import Iterable, List, Text

from behave.model import Row

def parse_context_table(headers: Iterable[Text], rows: Iterable[Row], clear: bool = True) -> List[dict]: # NOQA
    """
    Parses the table given by the behave context manager.
    Args:
        headers:
            Iterable with strings to serve as the keys for each row.
        rows:
            Iterable with row objects from the behave.model module.
        clear:
            Flag to wipe out false data types from the table

    Returns:
        A list with mappings for all the rows to the corresponding header.
        [
            {
                'heading1': 'row1_value1',
                'heading2': 'row1_value2'
            },
            {
                'heading1': 'row2_value1',
                'heading2': 'row2_value2'
            }
            [...]
        ]
    """
    if clear:
        return [{k: v for k, v in zip(headers, row) if v not in ['', None]}
                for row in rows]
    return [{k: v for k, v in zip(headers, row)} for row in rows]