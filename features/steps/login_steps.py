from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.wait_utils import wait_for_element_visible ,wait_for_element_clickable

@given("the user is on the OrangeHRM login page")
def step_open_login_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@when("the user enters the valid username and password")
def step_enter_credentials(context):
    wait_for_element_visible(context.driver, (By.NAME, "username"))
    context.driver.find_element(By.NAME, "username").send_keys("Admin")
    context.driver.find_element(By.NAME, "password").send_keys("admin123")

@when("clicks the login button")
def step_click_login(context):
    wait_for_element_clickable(context.driver, (By.XPATH, "//button[@type='submit']"))
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

@then("the user should see the dashboard")
def step_verify_dashboard(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )
    assert context.driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
