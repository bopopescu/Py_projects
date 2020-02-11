from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
# time.sleep(5)
# driver.close()
# driver.maximize_window()

from selenium.webdriver.common.by import By

#4. option-drop-down-menu: static/dynamic
# make sure there is select class in html

# <select class="form-control" id="exampleFormControlSelect1">
#                         <option>Male</option>
#                         <option>Female</option>
#                       </select>


gend_field = driver.find_element(By.ID, "exampleFormControlSelect1")
# gend_field = driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']")

locator = gend_field
text = 'Male'
sel = Select(locator)
sel.select_by_visible_text(text)
# sel.select_by_index(index) # index starts with 0 for first one
# sel.select_by_value(val)   # need to have value attribute to work

# sel.deselect_all()
# sel.deselect_by_index(index)
# sel.deselect_by_value(value)
# sel.deselect_by_visible_text(text)

time.sleep(5)
# find_option = driver.find_element_by_xpath("//option[text()='Male']")
find_option = driver.find_element_by_xpath("//select[contains(@id, 'Select1')]/option[2]")
find_option.click()

loop_option = driver.find_elements_by_xpath("//select[contains(@id, 'Select1')]/option")
print(len(loop_option))
for option_item in loop_option:
    print(option_item.text)

# <select class="form-control" id="exampleFormControlSelect1">
# #                         <option>Male</option>
# #                         <option>Female</option>
# #                       </select>
time.sleep(5)
driver.close()