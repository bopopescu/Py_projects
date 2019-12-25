from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


# locator actions
# send_keys("content"), click(), text,clear()
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
url = "https://rahulshettyacademy.com/angularpractice/"
# url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(2)
#@@ 1. static drop down
# tag: select
#  provide methods to  handle options in drop-down menu
item_select = driver.find_element_by_id("exampleFormControlSelect1")
dropdown = Select(item_select)

# 1.1 select_by_visible_text
text = "Female"
dropdown.select_by_visible_text(text)

time.sleep(2)
text = "Male"
dropdown.select_by_visible_text(text)
time.sleep(2)

# 1.2 select_by_index
dropdown.select_by_index(1)
time.sleep(1)
dropdown.select_by_index(0)

# 1.3 select_by_value

# @@ 2. Dynamic DropDown





time.sleep(2)
driver.close()


























































































