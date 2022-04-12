from abc import ABC


class BasePage(ABC):
    """
    Abstract class to serve as a base for all other page objects.
    Here is where to put all of the information relevant to all the screens
        (such as the header).
    """

    def __init__(self, driver):
        self.driver = driver
        self.url_base_page = 'https://training-wheels-protocol.herokuapp.com/'
