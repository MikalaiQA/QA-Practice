import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://www.qa-practice.com/elements/input')
    return driver




@pytest.fixture()
def page(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    param = request.param
    if param == 'alerts':
        driver.get('https://www.qa-practice.com/elements/alert/alert')
    elif param ==  'buttons':
        driver.get('https://www.qa-practice.com/elements/button/simple')
    elif param ==  'checkboxes':
        driver.get('https://www.qa-practice.com/elements/checkbox')
    elif param ==  'dragdrop':
        driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    elif param ==  'iframes':
        driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    elif param ==  'inputs':
        driver.get('https://www.qa-practice.com/elements/input')
    elif param ==  'newtab':
        driver.get('https://www.qa-practice.com/elements/new_tab')
    elif param ==  'popup':
        driver.get('https://www.qa-practice.com/elements/popup')
    elif param ==  'select':
        driver.get('https://www.qa-practice.com/elements/select')
    elif param ==  'textarea':
        driver.get('https://www.qa-practice.com/elements/textarea')
    yield driver


