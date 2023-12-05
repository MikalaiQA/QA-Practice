from selenium.webdriver.common.by  import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, args):
        return self.driver.find_element(*args)