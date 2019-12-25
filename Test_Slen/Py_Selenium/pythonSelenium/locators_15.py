from selenium import webdriver
import time

from selenium.webdriver import ActionChains
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
# url = "https://the-internet.herokuapp.com/iframe"
# url = "https://www.1point3acres.com/bbs/"
# url = "https://chercher.tech/practice/practice-pop-ups-selenium-webdriver"

url = "https://rahulshettyacademy.com/AutomationPractice"
driver.get(url)
# driver.maximize_window()

assert driver.find_element_by_id('displayed-text').is_displayed()

driver.find_element_by_id('hide-textbox').click()

assert not driver.find_element_by_id('displayed-text').is_displayed()

time.sleep(3)
driver.close()


























































































