from abc import ABC
from time import sleep

from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(ABC):
    """
    Classe abstrata para servir de base para todos os outros page objects.
    Aqui devem ser inseridas todas as informações relevantes para todas as telas
    """

    def __init__(self, driver):
        self.driver = driver
        self.url_base_page = 'https://training-wheels-protocol.herokuapp.com/'

        self._link_pages = {
            'Home Page': self.url_base_page,
            'Basic Auth': 'a[href="/basic_auth"]',
            'Checkboxes': 'a[href="/checkboxes"]',
            'Radio Buttons': 'a[href="/radios"]',
            'Drag and Drop': 'a[href="/drag_and_drop"]',
            'Dropdown': 'a[href="/dropdown"]',
            'Select2 - Uma opção': 'a[href="/apps/select2/single.html"]',
            'Select2 - Multiplas opções': 'a[href="/apps/select2/multi.html"]',
            'Controle Dinâmico': 'a[href="/dynamic_controls"]',
            'Upload de arquivos': 'a[href="/upload"]',
            'Login': 'a[href="/login"]',
            'Login com campo randômico': 'a[href="/login2"]',
            'Login com cadastro' :'a[href="/access"]',
            'Iframe bom': 'a[href="/nice_iframe"]',
            'Iframe ruim': 'a[href="/bad_iframe"]',
            'Hover': 'a[href="/hovers"]',
            'JavaScript Alerts': 'a[href="/javascript_alerts"]',
            'Modal com Sweet Alert': 'a[href="/sweet_alert"]',
            'Botões do teclado': 'a[href="/key_presses"]',
            'Nova janela': 'a[href="/windows"]',
            'Status code': 'a[href="/status_codes"]',
            'Tabelas': 'a[href="/tables"]',
            'Cadastro com Ajax': 'a[href="/games"]'
        }

        self._buttons = {}

        self._icons = {}

        self._actions = ActionChains(driver)
        self._wait = WebDriverWait(self.driver, 10)

    def select_page(self, page_name):
        page = self._link_pages[page_name]
        self._wait_to_exist(By.CSS_SELECTOR, page)
        page_selected = self._query_selector(page)
        page_selected.click()

    @property
    def actual_page_title(self):
        self._wait_to_exist(By.CSS_SELECTOR, 'div[class="example"] h3')
        text = self._query_selector('div[class="example"] h3').text
        return text

    def _wait_to_be_visible(self, element):
        return self._wait.until(ec.visibility_of(element))

    def _wait_any_element_to_exist(self, selector):
        return self._wait.until(ec.visibility_of_any_elements_located((By.CSS_SELECTOR, selector)))

    def _wait_to_exist(self, type_, locator):
        return self._wait.until(ec.presence_of_element_located((type_, locator)))

    def _wait_to_be_clickable(self, type_, locator):
        return self._wait.until(ec.element_to_be_clickable((type_, locator)))

    def _wait_url_to_match(self, pattern):
        return self._wait.until(ec.url_matches(pattern))

    def _query_selector(self, selector):
        try:
            if self._element_exists(selector):
                return self.driver.find_element(By.CSS_SELECTOR, selector)
        except NoSuchElementException:
            return f'{selector} elemento não encontrado, verifique'

    def _query_selector_all(self, selector):
        try:
            if self._element_exists(selector):
                self.driver.find_elements(By.CSS_SELECTOR, selector)
        except NoSuchElementException:
            return f'{selector} elementos não encontrados, verifique'

    def validate_exists(self, locator, selector):
        try:
            locator(By.CSS_SELECTOR, selector)
        except NoSuchElementException:
            return False
        return True

    def _elements_exists(self, selector):
        return self.validate_exists(self.driver.find_elements, selector)

    def _element_exists(self, selector):
        return self.validate_exists(self.driver.find_element, selector)

    def select_fields_text(self, element, text):
        select = Select(element)
        select.select_by_visible_text(text)

    def select_fields_value(self, element, value):
        sleep(1)
        select = Select(element)
        select.select_by_value(value)

    def click_button(self, button):
        try:
            self._wait_to_be_clickable(By.CSS_SELECTOR, self._buttons[button])
            self._query_selector(self._buttons[button]).click()
        except InvalidSelectorException:
            self._wait_to_be_clickable(By.XPATH, self._buttons[button])
            self.driver.find_element(By.XPATH, self.buttons[button]).click()
        except Exception as e:
            raise e

    def my_drag_and_drop(self, source, target):
        source1 = self._query_selector(source)
        target1 = self._query_selector(target)
        self._actions.drag_and_drop(source1, target1).perform()
        sleep(3)

    def reload_page(self):
        self.driver.refresh()

    def click_icon(self, icon):
        try:
            self.driver.execute_script(f"document.querySelector('{self.icons[icon]}').click()")
        except KeyError as e:
            raise e

    def execute_script(self, locator):
        try:
            self.driver.execute_script(f"document.querySelector('{locator}').click()")
        except KeyError as e:
            raise e