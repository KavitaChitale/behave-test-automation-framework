import logging
import os
import time
from utils.driver_helper import get_driver
from utils.logging_utils import take_screenshot, setup_logger

def before_all(context):
    context.driver = get_driver()
    os.makedirs("logs", exist_ok=True)
    log_filename = f'logs/test_run_{time.strftime("%Y%m%d-%H%M%S")}.log'
    log_level_str = os.getenv("LOG_LEVEL", "DEBUG").upper()
    log_levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }
    log_level = log_levels.get(log_level_str, logging.DEBUG)
    context.logger = setup_logger('test_logger', log_filename, level=log_level)

def after_all(context):
    pass

def after_scenario(context, scenario):
    if scenario.status == "failed":
        take_screenshot(context.driver, scenario.name)
    if hasattr(context, "driver"):
        context.driver.quit()
