from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser.get(link)
    button = browser.find_element_by_css_selector(".btn").click()
    alert = browser.switch_to.alert
    alert.accept()

    value_x = browser.find_element_by_css_selector("#input_value")
    x = value_x.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    input_field = browser.find_element_by_css_selector("#answer").send_keys(y)
    submit_btn = browser.find_element_by_css_selector(".btn").click()
    time.sleep(10)
finally:
    browser.quit()
