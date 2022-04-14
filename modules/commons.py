from typing import Iterable, List, Text

from behave.model import Row


from time import sleep

from modules.constants import URL_SUFFIXES

from selenium.webdriver.remote.webdriver import WebDriver


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


def check_url_suffix(driver: WebDriver, page_name: str) -> None:
    """
    Polls the current url to check if it loads into a page with the
    suffix.

    Args:
        driver:
            The current remote selenium webdriver.
        page_name:
            String with the text relative to the page name
            (key on the constant URL_SUFFIXES).
    """
    for i in range(5):
        try:
            suffix = driver.current_url.split('/')[-1]
            assert suffix.startswith(URL_SUFFIXES[page_name])
            return
        except AssertionError:
            sleep(.3)
    raise AssertionError('The page suffix was unnexpected')