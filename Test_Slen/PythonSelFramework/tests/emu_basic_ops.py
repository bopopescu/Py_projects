from selenium import webdriver
from selenium.webdriver.support.select import Select
import time, selenium
driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
# time.sleep(5)
# driver.close()
# driver.maximize_window()

from selenium.webdriver.common.by import By
print(f"selenium.__version__  is {selenium.__version__}")
# by_class_name can't have space
# name_text_field.is_displayed()
# is_displayed() --> visible on webpage

# name_text_field.is_enabled()
# simply means the element is working

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

# 0. is_displayed()
# <label>Name</label>
# name_field = driver.find_element_by_xpath("//label[text()='Name']")
# print(f"name_field is {name_field.text}")
# # name_field is Name
# try:
#     print(f"name_field displayed: {name_field.is_displayed()}")
#     # name_field displayed: True
# except:
#     print(f"name_field is NOT displayed")
# driver.close()

# 1. click(link)
# <a class="nav-link" href="/angularpractice/shop">Shop</a>
#  https://rahulshettyacademy.com/angularpractice
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

# selenium.common.exceptions.InvalidSelectorException: Message:



#
# 2
# Male
# Female

driver.set_page_load_timeout(60)
driver.get("https://www.finance.yahoo.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("yahoo_finance.png")
driver.find_element_by_name("yfin-usr-qry").send_keys("IBM")
driver.find_element_by_id("search-button").click()








