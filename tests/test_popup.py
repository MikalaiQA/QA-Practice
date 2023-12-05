import pytest   
from pages.base_page import BasePage
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time





@pytest.mark.parametrize('page', ['popup'], indirect=True)
def test_modal(page):
    page.find_element(By.XPATH, '//*[@data-bs-toggle="modal"]').click()
    page.find_element(By.XPATH, '//*[@class="form-check-label"]').click()
    page.find_element(By.XPATH, '//*[@form="id-checkbox-form"]').click()
    verif_text = page.find_element(By.XPATH, '//*[@class="result-text"]').text
    assert verif_text == 'select me or not'
    


@pytest.mark.parametrize('page', ['popup'], indirect=True)
def test_iframe_popup(page):
    page.find_element(By.XPATH, '//*[@href="/elements/popup/iframe_popup"]').click() #открывает айфрейм
    page.find_element(By.XPATH, '//*[@data-bs-toggle="modal"]').click() #открываем лаунч попап
    time.sleep(2)
    iframe = page.find_element(By.XPATH, "//iframe[contains(@class,'embed-responsive-item')]")
    page.switch_to.frame(iframe)
    copy_text = page.find_element(By.ID, "text-to-copy").text #копируем текст
    print(copy_text)
    page.switch_to.default_content()
    check_button = WebDriverWait(page, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Check"]')))
    check_button_1 = page.find_element(By.XPATH, '//button[text()="Check"]').click()  # нажимаем кнопку чек
    page.find_element(By.XPATH, '//*[@name="text_from_iframe"]').send_keys(copy_text)  #отправляем текст через переменную
    page.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()  #нажимаем кнопку сабмит
    verif_text = page.find_element(By.XPATH, '//*[@role="alert"]').text
    assert verif_text == 'Correct!'
    