import pytest   
from pages.base_page import BasePage
from selenium.webdriver.common.by  import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select




#Simple button page
@pytest.mark.parametrize('page', ['buttons'], indirect=True)
def test_simple_click(page):
    page.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()
    text_label = page.find_element(By.XPATH, '//*[@name="result"]').text
    assert 'Submitted' == text_label

#Looks like a button
@pytest.mark.parametrize('page', ['buttons'], indirect=True)
def test_looks_like_a_button_click(page):
    page.find_element(By.XPATH, '//*[@href="/elements/button/like_a_button"]').click()
    page.find_element(By.XPATH, '//*[@href="#"]').click()
    text_label = page.find_element(By.XPATH, '//*[@id="result-text"]').text
    assert 'Submitted' == text_label

#Disabled
@pytest.mark.parametrize('page', ['buttons'], indirect=True)
def test_disabled_select(page):
    page.find_element(By.XPATH, '//*[@href="/elements/button/disabled"]').click()
    dropdown = page.find_element(By.XPATH, '//*[@class="form-select"]')
    Select(dropdown).select_by_value("disabled")
    button = page.find_element(By.XPATH, '//*[@id="submit-id-submit"]').is_enabled()
    assert False == button

#enabled
@pytest.mark.parametrize('page', ['buttons'], indirect=True)
def test_enabled_select(page):
    page.find_element(By.XPATH, '//*[@href="/elements/button/disabled"]').click()
    dropdown = page.find_element(By.XPATH, '//*[@class="form-select"]')
    Select(dropdown).select_by_value("enabled")
    page.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()
    text_label = page.find_element(By.XPATH, '//*[@class="result"]').text
    assert 'Submitted' == text_label

