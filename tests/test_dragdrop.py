import pytest   
from pages.base_page import BasePage
from selenium.webdriver.common.by  import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.parametrize('page', ['dragdrop'], indirect=True)
def test_drag_drop_boxes(page):
    source_element = page.find_element(By.XPATH, '//*[@id="rect-draggable"]')
    target_element = page.find_element(By.XPATH, '//*[@id="rect-droppable"]')
    action_chains = ActionChains(page)
    action_chains.drag_and_drop(source_element, target_element).perform()
    verif_text =  page.find_element(By.XPATH, '//*[@id="text-droppable"]').text
    time.sleep(5)
    assert verif_text == 'Dropped!'