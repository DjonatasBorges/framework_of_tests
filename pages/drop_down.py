from pages.base import BasePage
from selenium.webdriver.common.by import By


class Dropdown(BasePage):
    def __init__(self, driver):
        super(Dropdown, self).__init__(driver)

        self.drop_down = '#dropdown'

        self._values_dropdown = {
            'Steve Rogers': '1',
            'Bucky': '2',
            'Tony Stark': '3',
            'Natasha Romanoff': '4',
            'Bruce Banner': '5',
            'Loki': '6',
            'Scott Lang': '7'
        }

    def selector_drop_down(self, name):
        heroe = self._values_dropdown[name]
        element = self.driver.find_element(By.CSS_SELECTOR, self.drop_down)
        all_options = element.find_elements(By.TAG_NAME, 'option')
        for option in all_options:
            if option.get_attribute("value") == heroe:
                option.click()

    def validate_element_drop_down(self, name):
        heroe = self._values_dropdown[name]
        element = self.driver.find_element(By.CSS_SELECTOR, self.drop_down)
        value = element.get_attribute("value")
        if heroe == value:
            return True
        else:
            return False
