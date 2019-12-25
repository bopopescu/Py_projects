from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
#
# alert = driver.switch_to.alert
# alert.accept()
# Java, javascript alert
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# url = "https://rahulshettyacademy.com/angularpractice/"
# url = "https://www.makemytrip.com/"
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
print(driver.title)
print(driver.current_url)
# driver.maximize_window()
time.sleep(2)
# @@ 4. popup
driver.find_element_by_css_selector("#name").send_keys("option3")
time.sleep(2)
driver.find_element_by_id("alertbtn").click()

time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
# alert.accept()
alert.dismiss()









time.sleep(2)
driver.close()


























































































