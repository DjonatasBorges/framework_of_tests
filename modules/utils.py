from __future__ import print_function

import functools
import os

from behave.model import ScenarioOutline


def patch_scenario_with_autoretry(scenario, max_attempts=3):

    def scenario_run_with_retries(scenario_run, scenario, *args, **kwargs):
        for attempt in range(1, max_attempts + 1):
            if not scenario_run(*args, **kwargs):
                if attempt > 1:
                    message = u"AUTO-RETRY SCENARIO PASSED (after {0} attempts)"
                    print(message.format(attempt))
                    retry_reports(scenario, attempt, message)
                return False    # -- NOT-FAILED = PASSED
            # -- SCENARIO FAILED:
            if attempt < max_attempts:
                print(u"AUTO-RETRY SCENARIO (attempt {0})".format(attempt))
        message = u"AUTO-RETRY SCENARIO FAILED (after {0} attempts)"
        print(message.format(max_attempts))
        return True

    if isinstance(scenario, ScenarioOutline):
        scenario_outline = scenario
        for scenario in scenario_outline.scenarios:
            scenario_run = scenario.run
            scenario.run = functools.partial(scenario_run_with_retries, scenario_run, scenario)
    else:
        scenario_run = scenario.run
        scenario.run = functools.partial(scenario_run_with_retries, scenario_run, scenario)

    def retry_reports(scenario, attempt, message):
        f = open(os.path.join(os.path.abspath('.'), 'reports', 'scenario_retry.txt'), "a+")
        f.write(str(scenario.name) + " " + message.format(attempt) + "\n")
        f.close()
