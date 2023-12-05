from pages.base_page import BasePage
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



button_selector = (By.ID, '')

class SimpleButtonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def button(self):
        return self.find(button_selector)