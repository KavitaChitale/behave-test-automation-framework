from utils.driver_helper import get_driver

def before_all(context):
    context.driver = get_driver()

def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()
