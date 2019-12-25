from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support       import expected_conditions as EC

# https://rahulshettyacademy.com/seleniumPractise/#/
# //div[@class='product-action']/button/parent::div/parent::div
#
#explicit wait:
#
# Not global, only apply for target execution

# HTML Inline Frame element (<iframe>)

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# url = "https://rahulshettyacademy.com/angularpractice/"
# url = "https://www.makemytrip.com/"
# url = "https://rahulshettyacademy.com/AutomationPractice/"
# driver.implicitly_wait(1000)
# url ="https://rahulshettyacademy.com/seleniumPractise/"

url = "https://the-internet.herokuapp.com/iframe"
driver.get(url)
# driver.maximize_window()
frame_id = "mce_0_ifr"
driver.switch_to.frame(frame_id)
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("QA Automation")

driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)



time.sleep(3)
# driver.close()


























































































