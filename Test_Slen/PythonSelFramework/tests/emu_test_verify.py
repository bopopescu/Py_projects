from selenium import webdriver
import selenium
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/angularpractice/"
# url = "https://www.lambdatest.com/"
driver.get(url)
# time.sleep(5)
# driver.close()
# driver.maximize_window()

from selenium.webdriver.common.by import By

# # <input class="form-control ng-untouched ng-pristine ng-invalid" minlength="2" name="name" required="" type="text">
# # <input class="form-control ng-untouched ng-dirty ng-valid" minlength="2" name="name" required="" type="text">
# name_text_field = driver.find_element(By.NAME, "name")
#
# print(selenium.__version__)
# # element.get_attribute('innerHTML')




#
# # 1. use relative path
# driver.save_screenshot('..\screenshot_1.png')
# # 2.
driver.get_screenshot_as_file('log_files\screenshot_ex.png')
# driver.get_screenshot_as_png()

time.sleep(5)
driver.close()