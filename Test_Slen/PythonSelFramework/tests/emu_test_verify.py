from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/angularpractice/"

driver.get(url)

from selenium.webdriver.common.by import By
# by_class_name can't have space
# name_text_field.is_displayed()
# name_text_field.is_enabled()
# name_text_field.is_selected()
# name_text_field.screenshot("filename")
# name_text_field.screenshot_as_png
# name_text_field.submit()

# sel.deselect_all()
# sel.deselect_by_index(index)
# sel.deselect_by_value(value)
# sel.deselect_by_visible_text(text)

# sel.select_by_visible_text(text)
# sel.select_by_index(index)
# sel.select_by_value(val)


# 1. click(link)
# <a class="nav-link" href="/angularpractice/shop">Shop</a>
#  https://rahulshettyacademy.com/angularpractice/shop
tmp_str=""
# driver.find_element_by_tag_name(tmp_str)
# driver.find_elements_by_tag_name(tmp_str)
#
# driver.find_element_by_id(tmp_str)
# driver.find_element_by_class_name(tmp_str)
# driver.find_element_by_name(tmp_str)
# driver.find_element_by_link_text(tmp_str)
# driver.find_element_by_partial_link_text(tmp_str)

# driver.find_element_by_xpath(tmp_str)
# driver.find_element_by_css_selector(tmp_str)

# driver.find_element(by, value)


# <a class="nav-link" href="/angularpractice/shop">Shop</a>
# shop_name = driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
# shop_name = driver.find_element(By.CSS_SELECTOR, "a[href='/angularpractice/shop']")
# shop_name = driver.find_element(By.LINK_TEXT, "Shop")
# shop_name = driver.find_element(By.PARTIAL_LINK_TEXT, "Sh")
# shop_name = driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']")



# shop_name = driver.find_element(By.CSS_SELECTOR, "a[class='nav-link']")  Not working, since class='nav-link'  not unique

# shop_name = driver.find_element(By.CLASS_NAME, "nav-link") # Not working

# shop_name.click()  #  https://rahulshettyacademy.com/angularpractice/shop

# 2. send_keys(text_field)
# <input class="form-control ng-untouched ng-pristine ng-invalid" minlength="2" name="name" required="" type="text">
# name_text_field = driver.find_element(By.NAME, "name")
# name_text_field = driver.find_element(By.CSS_SELECTOR, "input.form-control.ng-untouched.ng-pristine.ng-invalid")
# name_text_field = driver.find_element(By.CSS_SELECTOR, "input[class*='ng-invalid'")
name_text_field = driver.find_element(By.CSS_SELECTOR, "input[name*='nam'")
# name_text_field = driver.find_element(By.CSS_SELECTOR, "input[type='text'")
# name_text_field = driver.find_element(By.XPATH, "//input[@name='name']")
# name_text_field = driver.find_element(By.XPATH, "//input[@minlength='2']")



# Not working #name_text_field = driver.find_element(By.XPATH, "input//[@name='name']")
# selenium.common.exceptions.InvalidSelectorException: Message: invalid selector: Unable to locate an element with the xpath expression input//[@name='name'] because of the following error:
# SyntaxError: Failed to execute 'evaluate' on 'Document': The string 'input//[@name='name']' is not a valid XPath expression.

# not working: #name_text_field = driver.find_element(By.CLASS_NAME, "form-control ng-untouched ng-pristine ng-invalid")
# selenium.common.exceptions.NoSuchElementException
#


name_text_field.send_keys("ssqa_ssqaaa")
print(name_text_field.get_attribute("value"))
# time.sleep(1)
# name_text_field.clear()

# 3. click(checkbox)
# <input class="form-check-input" id="exampleCheck1" type="checkbox">
# checkbox_field = driver.find_element(By.ID, "exampleCheck1")
checkbox_field = driver.find_element(By.CLASS_NAME, "form-check-input")
# print(f"checkbox_field.is_selected() is {checkbox_field.is_selected()}")
# False
checkbox_field.click()
time.sleep(5)
# checkbox_field.
time.sleep(5)

# checkbox_field.screenshot_as_png

# print(f"checkbox_field.is_selected() is {checkbox_field.is_selected()}")
print(f"checkbox_field.is_selected() is {checkbox_field.get_attribute('checked')}")
# True
# checkbox_field.click()
# print(f"checkbox_field.is_selected() is {checkbox_field.is_selected()}")
# False
time.sleep(200)
#4. option-drop-down-menu: static/dynamic
# make sure there is select class in html
# <select class="form-control" id="exampleFormControlSelect1">
#                         <option>Male</option>
#                         <option>Female</option>
#                       </select>
gend_field = driver.find_element(By.ID, "exampleFormControlSelect1")
# gend_field = driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']")

locator = gend_field
text = 'Female'
sel = Select(locator)

sel.select_by_visible_text(text)
# sel.select_by_index(index) # index starts with 0 for first one
# sel.select_by_value(val)   # need to have value attribute to work

# sel.deselect_all()
# sel.deselect_by_index(index)
# sel.deselect_by_value(value)
# sel.deselect_by_visible_text(text)
time.sleep(200)
# 5. radio
# <input class="form-check-input" id="inlineRadio1" name="inlineRadioOptions" type="radio" value="option1">
radio_field = driver.find_element(By.CSS_SELECTOR, "input[value='option1']")
radio_field.click()
time.sleep(3)

radio_field_2 = driver.find_element(By.XPATH, "//input[@value='option2']")
radio_field_2.click()
time.sleep(1)

# 6. Date
# <input class="form-control" max="3000-12-31" min="1000-01-01" name="bday" type="date">
date_field = driver.find_element(By.CSS_SELECTOR, "input[type='date']")
date_field.send_keys("01/22/2020")


# . submit
# <input class="btn btn-success" type="submit" value="Submit">
# Not working# submit_field = driver.find_element(By.CLASS_NAME, "btn btn-success")
# submit_field = driver.find_element(By.XPATH, "//input[@class='btn btn-success']")
submit_field = driver.find_element(By.CSS_SELECTOR, "input[class*='btn-succ']")
submit_field = driver.find_element(By.XPATH, "//input[contains(@class,'btn-succ')]")
submit_field.click()



# . message_submit
# <div class="alert alert-success alert-dismissible">
submit_message = driver.find_element(By.CSS_SELECTOR, "div[class*='alert alert-success']")
alertText = submit_message.text
print(alertText)


time.sleep(5)
driver.close()