from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"

try:
    browser.get(link)
    num1 = browser.find_element_by_css_selector("#num1")
    num2 = browser.find_element_by_css_selector("#num2")
    num1_1 = int(num1.text)
    num2_1 = int(num2.text)
    summary = (num1_1 + num2_1)
    summary_1 = str(summary)
    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_visible_text(summary_1)
    button = browser.find_element_by_css_selector(".btn").click()
    time.sleep(10)
finally:
    browser.quit()
