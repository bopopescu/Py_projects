from selenium import webdriver
import time

# locator actions
# send_keys("content"), click(), text,clear()
# driver = webdriver.Chrome()
# Same test  cases work on Firefox too.
# No need to change
driver = webdriver.Firefox()
# url="https://rahulshettyacademy.com/angularpractice/"
url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
time.sleep(1)
print(driver.title)
print(driver.current_url)

time.sleep(1)
#@@ 1.find_element_by_name
find_name = driver.find_element_by_name("name")
find_name.send_keys("tester")
find_name = driver.find_element_by_name("email")
find_name.send_keys("ssqa@litepoint.com")

#@@ 2. find element by ID
find_id = driver.find_element_by_id("exampleCheck1")
find_id.click()

#@@ 3. class name: not recommended since hard to find unique one.
# find_classname = driver.find_element_by_class_name()

#@@ 4. css, need to be unique
# tagname[attribute="value"] --> Tagname optional
# <input class="form-control ng-untouched ng-pristine ng-invalid" minlength="2" name="name" required="" type="text">
# input[name='name']
# chrome->Console
# $("input[name='name']")
# java syntax: driver.findElementByName().sendKeys()
time.sleep(2)
find_css = driver.find_element_by_css_selector("input[name='name']")
find_css.clear()
find_css.send_keys("ssqa_test")

#@@ 5. Xpath
# //tagname[@attribute=value] ==> tagname optional
# //input[@type='submit']
# $x("//input[@type='submit']")
# [input.btn.btn-success]
# 0: input.btn.btn-success
# length: 1
# __proto__: Array(0)
xpath1 = "//input[@type='submit']"
xpath  = "//input[@class='btn btn-success']"
find_xpath = driver.find_element_by_xpath(xpath)
find_xpath.click()

#@@ 6.
show_text = driver.find_element_by_class_name("alert-success").text
# print(show_text)
# Success! The Form has been submitted successfully!.
assert "succzes" in show_text
#     assert "succzes" in show_text
# AssertionError

# customize css_selector tagname[attribute*='value']
css_select = "div[class*='alert-success']"
# show_text1  = driver.find_element_by_css_selector(css_select)
# print(show_text1.text)
#
# customize Xpath
# //tagname[contains(@attribute, 'value')]
xpath_custom = "//*[contains(@class, 'alert-success')]"
show_text2 = driver.find_element_by_xpath(xpath_custom)
print(show_text2.text)

time.sleep(5)
driver.close()

## Generate css from ID
# tagname#ID

