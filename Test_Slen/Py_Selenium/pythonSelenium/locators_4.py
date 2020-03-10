from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


# locator actions
# send_keys("content"), click(), text,clear()
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# url = "https://rahulshettyacademy.com/angularpractice/"
url = "https://www.makemytrip.com/"
driver.get(url)
print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(2)
# @@ 2. Dynamic DropDown
element = driver.find_element_by_id("fromCity")
element.click()
css_sel = "input[placeholder='From']"
css_selector = driver.find_element_by_css_selector(css_sel)
city_list = driver.find_elements_by_css_selector("p[class*='blackText']")
print(f"num of cities is {len(city_list)}")

css_selector.send_keys("del")
time.sleep(2)

city_list = driver.find_elements_by_css_selector("p[class*='blackText']")
print(f"num of cities is {len(city_list)}")
for c in city_list:
    if c.text  == "Delhi, India":
        # print(c.text)  Delhi, India
        c.click()
        time.sleep(2)
        break

destination = driver.find_element_by_xpath("//p[text()='Mumbai, India']")
time.sleep(2)
destination.click()
time.sleep(2)



time.sleep(2)
driver.close()


























































































