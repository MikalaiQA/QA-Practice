import pytest   
from pages.base_page import BasePage
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException








#Alert box
@pytest.mark.parametrize('page', ['alerts'], indirect=True)
def test_alert_box_closed(page):
    page.find_element(By.XPATH, '//*[@class="a-button"]').click()
    wait = WebDriverWait(page, 10)
    try:
        alert_wait = wait.until(EC.alert_is_present())
        alert = Alert(page)
        alert.accept()
        wait.until_not(EC.alert_is_present())

    except NoAlertPresentException:
        pass




#Confirmation box
@pytest.mark.parametrize('page', ['alerts'], indirect=True)
def test_confirmation_box_accept(page):
    page.find_element(By.XPATH, '//*[@href="/elements/alert/confirm"]').click()
    page.find_element(By.XPATH, '//*[@href="#"]').click()
    wait = WebDriverWait(page, 10)
    confirmation_wait = wait.until(EC.alert_is_present())
    confirmation = Alert(page)
    confirmation.accept()
    verif_text = page.find_element(By.XPATH, '//*[@id="result-text"]').text
    assert verif_text == 'Ok'




@pytest.mark.parametrize('page', ['alerts'], indirect=True)
def test_confirmation_box_cancel(page):
    page.find_element(By.XPATH, '//*[@href="/elements/alert/confirm"]').click()
    page.find_element(By.XPATH, '//*[@href="#"]').click()
    wait = WebDriverWait(page, 10)
    confirmation_wait = wait.until(EC.alert_is_present())
    confirmation = Alert(page)
    confirmation.dismiss()
    verif_text = page.find_element(By.XPATH, '//*[@id="result-text"]').text
    assert verif_text == 'Cancel'


#Prompt Box
@pytest.mark.parametrize('page', ['alerts'], indirect=True)
def test_prompt_box_accept(page):
    page.find_element(By.XPATH, '//*[@href="/elements/alert/prompt"]').click()
    page.find_element(By.XPATH, '//*[@href="#"]').click()
    wait = WebDriverWait(page, 10)
    prompt_wait = wait.until(EC.alert_is_present())
    prompt = Alert(page)
    prompt.send_keys("123123")
    prompt.accept()
    verif_text = page.find_element(By.XPATH, '//*[@id="result-text"]').text
    assert verif_text == '123123'


@pytest.mark.parametrize('page', ['alerts'], indirect=True)
def test_prompt_box_cancel(page):
    page.find_element(By.XPATH, '//*[@href="/elements/alert/prompt"]').click()
    page.find_element(By.XPATH, '//*[@href="#"]').click()
    wait = WebDriverWait(page, 10)
    prompt_wait = wait.until(EC.alert_is_present())
    prompt = Alert(page)
    prompt.dismiss()
    verif_text = page.find_element(By.XPATH, '//*[@id="result-text"]').text
    assert verif_text == 'You canceled the prompt'






 



