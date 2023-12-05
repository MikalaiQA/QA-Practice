import pytest   
from pages.base_page import BasePage
from selenium.webdriver.common.by  import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select





@pytest.mark.parametrize('page', ['select'], indirect=True)
def test_single_select(page):
    dropdown = page.find_element(By.XPATH, '//*[@name="choose_language"]')
    Select(dropdown).select_by_value("3")
    page.find_element(By.XPATH, '//*[@type="submit"]').click()
    verif_text = page.find_element(By.XPATH, '//*[@class="result-text"]').text
    assert verif_text == 'JavaScript'




@pytest.mark.parametrize('page', ['select'], indirect=True)
def test_multiple_select(page):
    page.find_element(By.XPATH, '//*[@href="/elements/select/mult_select"]').click()
    dropdown_1 = page.find_element(By.XPATH, '//*[@name="choose_the_place_you_want_to_go"]')
    Select(dropdown_1).select_by_value("1")
    dropdown_2= page.find_element(By.XPATH, '//*[@name="choose_how_you_want_to_get_there"]')
    Select(dropdown_2).select_by_value("3")
    dropdown_3 = page.find_element(By.XPATH, '//*[@name="choose_when_you_want_to_go"]')
    Select(dropdown_3).select_by_value("2")
    page.find_element(By.XPATH, '//*[@type="submit"]').click()
    verif_text = page.find_element(By.XPATH, '//*[@class="result-text"]').text
    assert verif_text == 'to go by train to the sea tomorrow'


