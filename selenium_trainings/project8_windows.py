from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser.get(link)
    button1 = browser.find_element_by_css_selector(".trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    value_x = browser.find_element_by_css_selector("#input_value")
    x = value_x.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    input_field = browser.find_element_by_css_selector("#answer").send_keys(y)
    button2 = browser.find_element_by_css_selector(".btn").click()
    time.sleep(10)

finally:
    browser.quit()
