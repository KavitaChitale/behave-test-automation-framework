from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)
