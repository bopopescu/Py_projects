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

url = "https://www.1point3acres.com/bbs/"
# class : ActionChains
# automate low level interations: mouse movement, mouse button actions
# key press, and context menu/submenu interation

driver.get(url)
# driver.maximize_window()

action = ActionChains(driver)
action.move_to_element(driver.find_element_by_link_text("板块分区")).perform()
action.move_to_element(driver.find_element_by_class_name("hidefocus")).click().perform()





time.sleep(3)
# driver.close()


























































































