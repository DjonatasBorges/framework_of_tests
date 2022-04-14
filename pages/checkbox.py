from pages.base import BasePage
from selenium.webdriver.common.by import By


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

    def confirm_movies(self, list_dict):
        lista = []
        dictionary = {}
        qtd_movies = 1
        for list in list_dict:
            values = list.values()
            for value in values:
                number_filme = f'Filme {qtd_movies}'
                for movie in self.checkbox.keys():
                    if movie in value:
                        dictionary.update({number_filme: movie})
                qtd_movies += 1
        return lista
