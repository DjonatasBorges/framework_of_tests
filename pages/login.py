from selenium.webdriver.common.by import By
from pages.base import BasePage


class Login(BasePage):
    def __init__(self, driver):
        super(Login, self).__init__(driver)
        self._user = '#userId'
        self._pwd = '#passId'
        self._msg_login = '#flash'

        self._buttons.update({
            'Login': 'button[type="submit"]',
            'Logout': "a[href='/logout']"
        })

    @property
    def user(self):
        return self._query_selector(self._user)

    @property
    def password(self):
        return self._query_selector(self._pwd)

    @property
    def msg_login(self):
        return self._query_selector(self._msg_login)

    def login(self, user, password):
        self._wait_to_exist(By.CSS_SELECTOR, self._user)
        self.user.send_keys(user)
        self.password.send_keys(password)
        self.click_button('Login')

    def confirm_login(self):
        self._wait_to_exist(By.CSS_SELECTOR, self._msg_login)
        msg = self.msg_login.text
        if 'Olá, Tony Stark. Você acessou a área logada!' in msg:
            return True
        return False

    def confirm_logout(self):
        self._wait_to_exist(By.CSS_SELECTOR, self._msg_login)
        mensagem = self.msg_login.text
        return mensagem

    def logout(self):
        self.click_button('Logout')
