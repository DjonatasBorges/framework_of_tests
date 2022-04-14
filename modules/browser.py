from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def setup_driver(browser, page):
    """
    Aplica o browser com os dados do guia do usuário que vem do behave.ini.
    """
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    driver.get(page)

    return driver
