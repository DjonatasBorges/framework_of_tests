from configparser import ConfigParser
from pages.login import Login

from pages.checkbox import Checkbox
from pages.drang_and_drop import DragAndDrop
from pages.drop_down import Dropdown

config = ConfigParser()
config.read('behave.ini')

APPLICATION_URL = config['behave.userdata']['page']

USERS = {
    'Usuário Correto': {
        'user': 'stark',
        'password': 'jarvis!'
    },

    'Usuário Incorreto': {
        'user': 'djonatas',
        'password': 'senha'
    }
}

PAGE_OBJECTS = {
    'Checkboxes': Checkbox,
    'Drag and Drop': DragAndDrop,
    'Dropdown': Dropdown,
    'Login': Login,
}

URL_SUFFIXES = {
    'Checkboxes': 'checkbox',
    'Drag and Drop': 'drag_and_drop',
    'Dropdown': 'dropdown',
    'Login': 'login'
}
