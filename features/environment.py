from modules.browser import setup_driver
from modules.utils import patch_scenario_with_autoretry

import os


def before_all(context):
    browser = context.config.userdata['browser']
    page = context.config.userdata['page']
    context.driver = setup_driver(browser, page)
    context.driver.maximize_window()

def before_scenario(context, scenario):
    if 'wip' in scenario.tags:
        scenario.skip('work in progress')

def after_step(context, step):
    debug = context.config.userdata['debug'].lower()

    if debug == 'true' and step.status == 'failed':
        """Starts ipdb debugger on step failure."""
        from ipdb import post_mortem
        post_mortem(step.exc_traceback)


def after_scenario(context, scenario):
    if scenario.status.name == 'failed':
        screenshot_file = '_'.join(scenario.name.split()) + "_failed.png"
        context.driver.get_screenshot_as_file(os.path.join(os.path.abspath('.'),
                                                           'reports', 'screenshots', screenshot_file))
    if not scenario.status.name == 'skipped':
        context.driver.get(context.config.userdata['page'])


def after_all(context):
    context.driver.close()


def before_feature(context, feature):
    if context.config.userdata.get('retry', 'false') == 'true':
        max_attempts = int(context.config.userdata.get('max_retry_attempts', '3'))
        for scenario in feature.walk_scenarios():
            patch_scenario_with_autoretry(scenario, max_attempts=max_attempts)