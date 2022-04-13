from time import sleep

from pages.base import BasePage


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_selection_state_to_be


class Checkbox(BasePage):
    def __init__(self, driver):
        super(Checkbox, self).__init__(driver)

        self.checkbox = {
            'Capitão América: O Primeiro Vingador': 'input[value="cap"]',
            'Homem de Ferro': 'input[value="iron-man"]', 
            'Thor': '#thor', 
            'Os Vingadores': 'input[value="the-avengers"]', 
            'Guardiões da Galáxia': 'input[value="guardians"]', 
            'Homem-Formiga': 'input[value="ant-man"]', 
            'Pantera Negra': 'input[value="black-panther"]', 
        }

    def deselect_all_checkboxes(self):
        for i in self.checkbox.values():
            if self.driver.find_element(By.CSS_SELECTOR, i).is_selected():
                self._query_selector(f'{i}').click()

    def select_checkbox(self, names):
        for name in names:
            locator = self.checkbox[name]
            if not self.driver.find_element(By.CSS_SELECTOR, locator).is_selected():
                self._query_selector(locator).click()

    def confirm_movies(self, movies):
        strings = ''
        for movie in movies:
            locator = self.checkbox[movie]
            if self.driver.find_element(By.CSS_SELECTOR, locator).is_selected():
                strings.join(f'{self.driver.find_element(By.CSS_SELECTOR, locator)}, ')
        return strings