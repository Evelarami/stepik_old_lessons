from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser.get(link)
    treasure = browser.find_element_by_css_selector("#treasure")
    x_element = treasure.get_attribute("valuex")


    def calc(x_element):
        return str(math.log(abs(12 * math.sin(int(x_element)))))


    y = calc(x_element)
    input_value = browser.find_element_by_css_selector("#answer").send_keys(y)
    robotCheckbox = browser.find_element_by_css_selector("#robotCheckbox").click()
    robotRadiobutton = browser.find_element_by_css_selector("#robotsRule").click()
    submit_button = browser.find_element_by_css_selector(".btn").click()

    time.sleep(10)

finally:
    browser.quit()

