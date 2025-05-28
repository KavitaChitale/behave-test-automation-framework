from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.wait_utils import wait_for_element_visible, wait_for_element_clickable, wait_for_element_present


@given("the user is on the OrangeHRM login page")
def step_open_login_page(context):
    context.logger.info("Navigating to the OrangeHRM login page.")
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@when("the user enters the valid username and password")
def step_enter_credentials(context):
    context.logger.debug("Waiting for username input to be visible.")
    wait_for_element_visible(context.driver, (By.NAME, "username"))
    context.driver.find_element(By.NAME, "username").send_keys("Admin")
    context.driver.find_element(By.NAME, "password").send_keys("admin123")
    context.logger.info("Entered valid username and password.")

@when("clicks the login button")
def step_click_login(context):
    context.logger.debug("Waiting for the login button to be clickable.")
    wait_for_element_clickable(context.driver, (By.XPATH, "//button[@type='submit']"))
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    context.logger.info("Clicked the login button.")

@then("the user should see the dashboard")
def step_verify_dashboard(context):
    context.logger.debug("Verifying the dashboard is visible.")
    wait_for_element_present(context.driver, (By.XPATH, "//h6[text()='Dashboard']"))
    assert context.driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
    context.logger.info("Dashboard is successfully displayed.")
