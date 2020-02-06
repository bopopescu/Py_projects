from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

# 1. Handle auto-suggestive drop-down menu
driver = webdriver.Chrome()
url = "https://www.makemytrip.com/"
driver.get(url)
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
for city in cities:
    if "Del Rio" in city.text:
        print(city.text)
        city.click()
        time.sleep(2)
        destination_field = driver.find_element(By.XPATH, "//p[text()='Delhi, India']")
        destination_field.click()

# 2.



time.sleep(1)
driver.close()