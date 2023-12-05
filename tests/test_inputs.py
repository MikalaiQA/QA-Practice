import pytest   
from pages.base_page import BasePage
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import keys






#Text Input
@pytest.mark.parametrize('page', ['inputs'], indirect=True)
def test_text_field_title(page):
    text_label = page.find_element(By.XPATH, '//*[@for="id_text_string"]').text
    assert  'Text string*' == text_label

@pytest.mark.parametrize('page', ['inputs'], indirect=True)
def test_text_field_inputs_submit(page):
    page.find_element(By.XPATH, '//*[@id="id_text_string"]').send_keys('123qwe')
    page.find_element(By.XPATH, '//*[@id="id_text_string"]').send_keys(u'\ue007')         #send_keys(u'\ue007')  == #send_keys(Keys.ENTER)  
    text_validation = page.find_element(By.XPATH, '//*[@id="result-text"]').text
    assert '123qwe' == text_validation

@pytest.mark.parametrize('page', ['inputs'], indirect=True)
def test_text_field_max_characters(page):
    page.find_element(By.XPATH, '//*[@id="id_text_string"]').send_keys('123456789012345678901234567890')
    page.find_element(By.XPATH, '//*[@id="id_text_string"]').send_keys(u'\ue007')         #send_keys(u'\ue007')  == #send_keys(Keys.ENTER)  
    text_validation = page.find_element(By.XPATH, '//*[@class="invalid-feedback"]').text
    assert 'Please enter no more than 25 characters' == text_validation

@pytest.mark.parametrize('page', ['inputs'], indirect=True)
def test_text_field_min_characters(page):
    page.find_element(By.XPATH, '//*[@id="id_text_string"]').send_keys('1')
    page.find_element(By.XPATH, '//*[@id="id_text_string"]').send_keys(u'\ue007')         #send_keys(u'\ue007')  == #send_keys(Keys.ENTER)  
    text_validation = page.find_element(By.XPATH, '//*[@class="invalid-feedback"]').text
    assert 'Please enter 2 or more characters' == text_validation

#Email field
@pytest.mark.parametrize('page', ['inputs'], indirect=True)
def test_email_title(page):
    page.find_element(By.XPATH, '//*[@href="/elements/input/email"]').click()
    text_label = page.find_element(By.XPATH, '//*[@for="id_email"]').text
    assert  'Email*' == text_label

@pytest.mark.parametrize('page', ['inputs'], indirect=True)
def test_email_is_valid(page):
    page.find_element(By.XPATH, '//*[@href="/elements/input/email"]').click()
    page.find_element(By.XPATH, '//*[@id="id_email"]').send_keys('12345@gmail.com')
    page.find_element(By.XPATH, '//*[@id="id_email"]').send_keys(u'\ue007')         #send_keys(u'\ue007')  == #send_keys(Keys.ENTER)  
    text_label = page.find_element(By.XPATH, '//*[@id="result-text"]').text      
    assert  '12345@gmail.com' == text_label

@pytest.mark.parametrize('page', ['inputs'], indirect=True)
def test_email_is_not_valid(page):
    page.find_element(By.XPATH, '//*[@href="/elements/input/email"]').click()
    page.find_element(By.XPATH, '//*[@id="id_email"]').send_keys('153')
    page.find_element(By.XPATH, '//*[@id="id_email"]').send_keys(u'\ue007')         #send_keys(u'\ue007')  == #send_keys(Keys.ENTER)  
    text_label = page.find_element(By.XPATH, '//*[@class="invalid-feedback"]').text      
    assert  'Enter a valid email address.' == text_label

@pytest.mark.parametrize('page', ['inputs'], indirect=True)
def test_localhost_email(page):
    page.find_element(By.XPATH, '//*[@href="/elements/input/email"]').click()
    page.find_element(By.XPATH, '//*[@id="id_email"]').send_keys('12345@localhost')
    page.find_element(By.XPATH, '//*[@id="id_email"]').send_keys(u'\ue007')         #send_keys(u'\ue007')  == #send_keys(Keys.ENTER)  
    text_label = page.find_element(By.XPATH, '//*[@id="result-text"]').text      
    assert  '12345@localhost' == text_label



#Password field
@pytest.mark.parametrize('page', ['inputs'], indirect=True)
def test_password_title(page):
    page.find_element(By.XPATH, '//*[@href="/elements/input/passwd"]').click()
    text_label = page.find_element(By.XPATH, '//*[@for="id_password"]').text
    assert  'Password*' == text_label

@pytest.mark.parametrize('page', ['inputs'], indirect=True)
def test_password_is_valid(page):
    page.find_element(By.XPATH, '//*[@href="/elements/input/passwd"]').click()
    page.find_element(By.XPATH, '//*[@id="id_password"]').send_keys('12345Qw$')
    page.find_element(By.XPATH, '//*[@id="id_password"]').send_keys(u'\ue007')         #send_keys(u'\ue007')  == #send_keys(Keys.ENTER)   //*[@id="result-text"]
    text_label = page.find_element(By.XPATH, '//*[@id="result-text"]').text
    assert  '12345Qw$' == text_label

@pytest.mark.parametrize('page', ['inputs'], indirect=True)
def test_password_is_not_valid_1(page):
    page.find_element(By.XPATH, '//*[@href="/elements/input/passwd"]').click()
    page.find_element(By.XPATH, '//*[@id="id_password"]').send_keys('12')
    page.find_element(By.XPATH, '//*[@id="id_password"]').send_keys(u'\ue007')         #send_keys(u'\ue007')  == #send_keys(Keys.ENTER)   //*[@id="result-text"]
    text_label = page.find_element(By.XPATH, '//*[@class="invalid-feedback"]').text
    assert  'Low password complexity' == text_label

@pytest.mark.parametrize('page', ['inputs'], indirect=True)
def test_password_is_not_valid_2(page):
    page.find_element(By.XPATH, '//*[@href="/elements/input/passwd"]').click()
    page.find_element(By.XPATH, '//*[@id="id_password"]').send_keys('1234$Qw')
    page.find_element(By.XPATH, '//*[@id="id_password"]').send_keys(u'\ue007')         #send_keys(u'\ue007')  == #send_keys(Keys.ENTER)   //*[@id="result-text"]
    text_label = page.find_element(By.XPATH, '//*[@class="invalid-feedback"]').text
    assert  'Low password complexity' == text_label