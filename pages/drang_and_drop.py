from pages.base import BasePage
from selenium.webdriver.common.by import By


class DragAndDrop(BasePage):
    def __init__(self, driver):
        super(DragAndDrop, self).__init__(driver)

        self._team_stark = '#columns > div.col-md-6.team-stark > h5:nth-child(2) > div'
        self._team_cap = "#columns > div.col-md-6.team-cap > h5:nth-child(2) > div"
        self._spider_man = 'img[alt="Homem Aranha"]'

        self._locators_team = {
            "Time do Stark": self._team_stark ,
            "Time do Capitão América": self._team_cap
        }

        self._locators_heroes = {
            "Homem-Aranha": self._spider_man
        }

    def drag_and_drop(self, heroe, team):
        source = self._locators_heroes[heroe]
        target = self._locators_team[team]
        self.my_drag_and_drop(source, target)

    def confirm_position_hero(self, heroe, team):
        locator = f'{self._locators_team[team]} {self._locators_heroes[heroe]}'
        confirm_return = self.driver.find_element(By.CSS_SELECTOR, locator)
        if confirm_return:
            return True
        return False
        

