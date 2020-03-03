from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import  selenium
driver = webdriver.Chrome()
# url = "https://rahulshettyacademy.com/angularpractice/"
# print(f"selenium.__version__  is {selenium.__version__}") #  3.141.0
# driver.maximize_window()
# driver.get(url)

# 1. click on link
# Verify with some typical element in the new page

url  = "https://rahulshettyacademy.com/angularpractice"
driver.get(url)
# <a class="nav-link" href="/angularpractice/shop">Shop</a>
# print(driver.current_url)
# shop_item = driver.find_element(By.LINK_TEXT, "Shop")
# shop_item = driver.find_element(By.PARTIAL_LINK_TEXT, "Sh")
# shop_item = driver.find_element(By.CSS_SELECTOR, 'a[href*="/shop"]')
# shop_name = driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']")

shop_item = driver.find_element(By.XPATH, "//a[contains(@href,'shop')]")
# shop_item.click()
# <h1 class="my-4">Shop Name</h1>
# page_verify = driver.find_element_by_class_name("my-4")
# print("Shop Name" in page_verify.text )
# print(driver.current_url)
# https://rahulshettyacademy.com/angularpractice/shop
#

# 2. send_keys(text_field)
# Verified with get_attribute("value")

# <input class="form-control ng-untouched ng-pristine ng-invalid" minlength="2" name="name" required="" type="text">
# name_text_field = driver.find_element(By.CSS_SELECTOR, "input[class='form-control ng-untouched ng-pristine ng-invalid'")
# name_text_field = driver.find_element(By.CSS_SELECTOR, "input.form-control.ng-untouched.ng-pristine.ng-invalid")
# name_text_field = driver.find_element(By.CSS_SELECTOR, "input[class*='ng-invalid'")
# name_text_field = driver.find_element(By.XPATH, "//input[@name='name']")
# name_text_field = driver.find_element(By.XPATH, "//input[@minlength='2']")

name_field = driver.find_element(By.NAME, "name")
# name_field.send_keys("ssqa_ssqaaa")
# page_verify = name_field.get_attribute("value") == "ssqa_ssqaaa"
# print(page_verify)
# time.sleep(1)
# name_field.clear()

# 3.    checkbox
# is_selected()
# get_attribute('checked')

# <input class="form-check-input" id="exampleCheck1" type="checkbox">
# checkbox_field = driver.find_element(By.ID, "exampleCheck1")

# checkbox_field = driver.find_element(By.CLASS_NAME, "form-check-input")
# print(f"checkbox_field.is_selected() is {checkbox_field.is_selected()}")
# False
# checkbox_field.click()
# print(f"checkbox_field.is_selected() is {checkbox_field.is_selected()}")
# True
# print(f"checkbox_field.is_selected() is {checkbox_field.get_attribute('checked')}")
# True

# 4. radio
# Verified with is_selected()

# <input class="form-check-input" id="inlineRadio1" name="inlineRadioOptions" type="radio" value="option1">
radio_field = driver.find_element(By.CSS_SELECTOR, "input[value='option1']")
# radio_field.click()

# radio_field_2 = driver.find_element(By.XPATH, "//input[@value='option2']")
# print(f"radido_field_2 is  Selected: {radio_field_2.is_selected()}") # False
# radio_field_2.click()
# print(f"radido_field_2 is  Selected: {radio_field_2.is_selected()}") # True
# time.sleep(1)

# 5. submit
# print("Success!" in page_verify.text)
# print(page_verify.text)

# <input class="btn btn-success" type="submit" value="Submit">

# Not working# submit_field = driver.find_element(By.CLASS_NAME, "btn btn-success")
# submit_field = driver.find_element(By.XPATH, "//input[@class='btn btn-success']")
# submit_field = driver.find_element(By.CSS_SELECTOR, "input[class*='btn-succ']")
submit_field = driver.find_element(By.XPATH, "//input[contains(@class,'btn-succ')]")
# submit_field.click()
# <div class="alert alert-success alert-dismissible">
#                     <a aria-label="close" class="close" data-dismiss="alert" href="#">×</a>
#                     <strong>Success!</strong> The Form has been submitted successfully!.
#                   </div>
# page_verify = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
# page_verify = driver.find_element(By.CSS_SELECTOR, "div[class*='alert alert-success']")
# page_verify = driver.find_element(By.CLASS_NAME, "alert")
# print("Success!" in page_verify.text)
# print(page_verify.text)

# 6. Date
# <input class="form-control" max="3000-12-31" min="1000-01-01" name="bday" type="date">
date_field = driver.find_element(By.CSS_SELECTOR, "input[type='date']")
date_field.send_keys("01/22/2020")

# 7. Drop Down Menu
# 1.)
# Dropdown are formed using select tag in html,
# if dropdown is not formed with select tag,
# you cannot use this Select Class methods present in python selenium

# menu_verify =  menu_field.get_attribute("value") #  Female
# make sure there is select class in html
# <select class="form-control" id="exampleFormControlSelect1">
#                         <option>Male</option>
#                         <option>Female</option>
#                       </select>

# Option with value  in html
# <option value="foo">Bar1</option>


# menu_field = driver.find_element(By.ID, "exampleFormControlSelect1")
# menu_field = driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']")
menu_field = driver.find_element(By.CSS_SELECTOR, "select#exampleFormControlSelect1")
# print("this is text", type(menu_field.text)) #  str
# str_list = list(menu_field.text) # male, \n, Female \n

menu_select = Select(menu_field)
# print(f"options {type(menu_select.options)}") # list
# print(menu_select.options[0].text) # Male

# text = 'Female'
# menu_select.select_by_visible_text(text)
# # sel.select_by_index(index) # index starts with 0 for first one
# # sel.select_by_value(val)   # need to have value attribute to work
#
# menu_verify =  menu_field.get_attribute("value") #  Female
# print(menu_verify)

# time.sleep(5)
# find_option = driver.find_element_by_xpath("//option[text()='Male']")
# find_option.click()
#
# loop_option = driver.find_elements_by_xpath("//select[contains(@id, 'Select1')]/option")
# print(len(loop_option))
# for option_item in loop_option:
#     print(option_item.text)

# 2.) Deselect
# menu_select.deselect_all()
# menu_select.deselect_by_index(index)
# menu_select.deselect_by_value(value)
# menu_select.deselect_by_visible_text(text)

































#
time.sleep(2)
driver.close()