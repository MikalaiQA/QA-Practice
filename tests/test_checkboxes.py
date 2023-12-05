import pytest   
from pages.base_page import BasePage
from selenium.webdriver.common.by  import By
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize('page', ['checkboxes'], indirect=True)
def test_single_checkbox_select(page):
    page.find_element(By.XPATH, '//*[@type="checkbox"]').click()
    page.find_element(By.XPATH, '//*[@type="submit"]').click()
    verif_text = page.find_element(By.XPATH, '//*[@class="result-text"]').text
    assert verif_text == 'select me or not'





@pytest.mark.parametrize('page', ['checkboxes'], indirect=True)
def test_checkboxes_select(page):
    page.find_element(By.XPATH, '//*[@href="/elements/checkbox/mult_checkbox"]').click()
    page.find_element(By.XPATH, '//*[@value="one"]').click() #one
    page.find_element(By.XPATH, '//*[@value="two"]').click() #two
    page.find_element(By.XPATH, '//*[@value="three"]').click() #three
    page.find_element(By.XPATH, '//*[@type="submit"]').click()
    verif_text = page.find_element(By.XPATH, '//*[@class="result-text"]').text
    assert verif_text == 'one, two, three'





