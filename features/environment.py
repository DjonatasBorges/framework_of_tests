from modules.browser import setup_driver

def before_all(context):
    browser = context.config.userdata['browser']
    page = context.config.userdata['page']
    context.driver = setup_driver(browser, page)
    context.driver.maximize_window()

def after_all(context):
    context.driver.close()
