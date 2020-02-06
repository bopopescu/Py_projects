from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

# 1. explicit wait is not global, it is only for certain element
# 2. implicit wait is global, for each element, poll DOM periodically until timeout


driver = webdriver.Chrome()
url = "http://the-internet.herokuapp.com/iframe"
driver.get(url)
driver.implicitly_wait(2)

# default content
print(driver.find_element_by_tag_name("h3").text)
# frame id, frame name
driver.switch_to.frame("mce_0_ifr")
# text_field = driver.find_element_by_xpath("//[text()='Your content goes here.'")
text_field = driver.find_element_by_css_selector("body#tinymce")
# text_field.click()
text_field.clear()
text_field.send_keys("Test in in process!!!")
# print(driver.find_element_by_tag_name("h3").text)
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)

time.sleep(3)
driver.close()