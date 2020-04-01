from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time


# 1. Handle auto-suggestive drop-down menu
driver = webdriver.Chrome()
url = "https://www.makemytrip.com/"
driver.implicitly_wait(10)
driver.get(url)

# step 1: click
# <input data-cy="fromCity" id="fromCity" type="text" class="fsw_inputField font30 lineHeight36 latoBlack" readonly="" value="Del Rio">
driver.find_element_by_id("fromCity").click()

# step 2: send_keys
# <input type="text" autocomplete="off" aria-autocomplete="list" aria-controls="react-autowhatever-1" class="react-autosuggest__input react-autosuggest__input--open" placeholder="From" value="">

driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")

# step 1 and step 2 can be combined with one step
# fill in textbox, no need to click first ,just use send_keys
# driver.find_element_by_id("fromCity").send_keys("del")


# <p class="font14 appendBottom5 blackText">Delhi, India</p>
from_city = driver.find_element_by_xpath("//p[text()='Delhi, India']")
print(f"from {from_city.text}")
from_city.click()

# time.sleep(5)

# <input type="text" autocomplete="off" aria-autocomplete="list" aria-controls="react-autowhatever-1" class="react-autosuggest__input react-autosuggest__input--open" placeholder="To" value="">
driver.find_element_by_css_selector("input[placeholder='To']").send_keys("mu")

# <p class="font14 appendBottom5 blackText">Del Rio, United States</p>
# <p class="font14 appendBottom5 blackText">Mumbai, India</p>
to_city = driver.find_element_by_xpath("//p[text()='Mumbai, India']")
print(f"to_city: {to_city.text}")
to_city.click()

# <div class="DayPicker-Day DayPicker-Day--selected" tabindex="-1" role="gridcell" aria-label="Fri Mar 06 2020" aria-disabled="false" aria-selected="true">
#   <div class="dateInnerCell">
#       <p>6</p>
#   </div>
# </div>
date_field = driver.find_element_by_xpath("//div[@aria-label='Fri Mar 06 2020']/div/p")
print(date_field.text)
date_field.click()
# from Delhi, India
# to_city: Mumbai, India
# 6

# 2.

time.sleep(10)
driver.close()