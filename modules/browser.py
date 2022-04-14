from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def setup_driver(browser, page):
    """
    Sets up the browser with the given the user_data.
    """
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    driver.get(page)

    return driver
