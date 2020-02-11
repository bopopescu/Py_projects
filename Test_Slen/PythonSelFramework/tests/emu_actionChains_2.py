from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
# ActionChains
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
url = "https://chercher.tech/practice/practice-pop-ups-selenium-webdriver"
driver.get(url)
driver.implicitly_wait(2)

action = ActionChains(driver)
# right-click, then inspect
# <input type="button" id="double-click" value="Double Click Me">
action.double_click(driver.find_element_by_id("double-click")).perform()

time.sleep(2)
alert = driver.switch_to.alert
print(alert.text) # You double clicked me!!!, You got to be kidding me
alert.accept()

# driver.switch_to.alert
# driver.switch_to.default_content()
# driver.switch_to.frame()
# driver.switch_to.parent_frame()
# driver.switch_to.window()

time.sleep(3)
driver.close()