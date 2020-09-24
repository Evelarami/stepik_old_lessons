from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("starting browser for testing...")
    browser = webdriver.Chrome()
    yield browser
    print("quit browser.")
    browser.quit()


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_parametrize_on_page(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    print("/nhere starts implicitly wait")
    browser.implicitly_wait(10)
    text_area = browser.find_element_by_css_selector(".textarea")
    text_area.send_keys(str(answer))
    print("searching of button")
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    smart_hints = browser.find_element_by_css_selector(".smart-hints__hint")
    assert "Correct!" in smart_hints.text
