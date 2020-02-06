from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
# JavaScript executor --2
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
driver.maximize_window()
time.sleep(1)
driver.implicitly_wait(2)
shopbutton  = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click()", shopbutton)

time.sleep(2)
# Scroll down with  Javascript
# from top of the page to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")





time.sleep(3)
driver.close()