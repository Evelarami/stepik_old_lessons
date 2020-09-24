from selenium import webdriver
import math
import time
try:
    browser = webdriver.Chrome()
    link = browser.get("http://suninjuly.github.io/math.html")

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)

    input_label = browser.find_element_by_css_selector("#answer").send_keys(y)
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    radiobutton = browser.find_element_by_css_selector("[value='robots']").click()
    button = browser.find_element_by_css_selector(".btn").click()

finally:
    time.sleep(10)
    browser.quit()

