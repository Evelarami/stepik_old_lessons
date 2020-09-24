from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_css_selector(".btn").click()
    x_value = browser.find_element_by_css_selector("#input_value")
    x = x_value.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    input_field = browser.find_element_by_css_selector("#answer").send_keys(y)
    button = browser.find_element_by_css_selector("#solve").click()
    time.sleep(10)

finally:
    browser.quit()
