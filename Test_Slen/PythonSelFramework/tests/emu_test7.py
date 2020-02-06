from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

# 1. Javascript pop ups

driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
driver.implicitly_wait(4)

alert_field = driver.find_element(By.CSS_SELECTOR, "input#name")
alert_field.send_keys("options 4")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
time.sleep(1)
print(alert.text)
valid_text = "option"
# assert valid_text in alert.text

# Hello options 4, share this practice page and share your knowledge
# alert.accept() # Ok
alert.dismiss() # Cancel
time.sleep(1)
driver.close()