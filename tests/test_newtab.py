import pytest   
from pages.base_page import BasePage
from selenium.webdriver.common.by  import By



@pytest.mark.parametrize('page', ['newtab'], indirect=True)
def test_link_newtab(page):
    main_window_handle = page.current_window_handle
    page.find_element(By.XPATH, '//*[@href="/elements/new_tab/new_page"]').click()
    
    # Ожидание нового окна (вкладки)
    new_window_handle = None
    for handle in page.window_handles:
        if handle != main_window_handle:
            new_window_handle = handle
            break
    
    page.switch_to.window(new_window_handle)
    verif_text = page.find_element(By.XPATH, '//*[@class="result-text"]').text
    assert verif_text == 'I am a new page in a new tab'



