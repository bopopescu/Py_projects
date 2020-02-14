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

# <input class="form-control ng-untouched ng-pristine ng-invalid" minlength="2" name="name" required="" type="text">
# <input class="form-control ng-untouched ng-dirty ng-valid" minlength="2" name="name" required="" type="text">
name_text_field = driver.find_element(By.NAME, "name")



with open('html_element.html', 'w') as f:
    f.write(name_text_field.get_attribute('outerHTML'))

with  open("html_src_code.html", "w", encoding="utf-8") as fout:
    fout.write(driver.page_source)


name_text_field.send_keys("ssqa_ssqaaa")
print(name_text_field.get_attribute("value"))
print(name_text_field.get_attribute("outerHTML"))
print(name_text_field.get_attribute("innerHTML"))
# element.get_attribute('innerHTML')
time.sleep(5)
driver.close()