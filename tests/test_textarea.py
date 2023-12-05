import pytest   
from pages.base_page import BasePage
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select






@pytest.mark.parametrize('page', ['textarea'], indirect=True)
def test_text_area(page):
    page.find_element(By.XPATH, '//*[@name="text_area"]').send_keys(' sadfasddfasdfsafdas dfa sdfasdfa sfsadfasdfsa ')
    page.find_element(By.XPATH, '//*[@type="submit"]').click()
    verif_text = page.find_element(By.XPATH, '//*[@class="result-chapters"]').text
    assert verif_text == 'sadfasddfasdfsafdas dfa sdfasdfa sfsadfasdfsa'





@pytest.mark.parametrize('page', ['textarea'], indirect=True)
def test_multiple_text_area(page):
    page.maximize_window()
    page.find_element(By.XPATH, '//*[@href="/elements/textarea/textareas"]').click()
    page.find_element(By.XPATH, '//*[@name="first_chapter"]').send_keys('12')
    page.find_element(By.XPATH, '//*[@name="second_chapter"]').send_keys('24')
    page.find_element(By.XPATH, '//*[@name="third_chapter"]').send_keys('36')
    wait = WebDriverWait(page, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-id-submit"]')))
    page.execute_script("window.scrollBy(10000, 0);")
    element.click()
    verif_text = page.find_element(By.XPATH, '//*[@class="result-chapters"]').text
    assert verif_text == '12\n24\n36'