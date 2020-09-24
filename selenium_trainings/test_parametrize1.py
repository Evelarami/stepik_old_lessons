from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def browser():
    print("/nstarting browser..")
    browser = webdriver.Chrome()
    yield browser
    print("/nquit browser")
    browser.quit()


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
