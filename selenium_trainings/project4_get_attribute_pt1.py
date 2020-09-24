from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots radio", robots_radio)
    assert robots_checked is None

    button = browser.find_element_by_css_selector(".btn")
    button_disabled = button.get_attribute("disabled")
    print("value of Submit button", button_disabled)
    assert button_disabled is None

    time.sleep(15)
    button_disabled = button.get_attribute("disabled")
    print("value of Submit button after 10 sec", button_disabled)
    assert button_disabled is not None

finally:
    browser.quit()