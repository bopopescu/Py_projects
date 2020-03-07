from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

# 1. explicit wait is not global, it is only for certain element
# 2. implicit wait is global, for each element, poll DOM periodically until timeout


driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/seleniumPractise"
driver.get(url)
driver.implicitly_wait(14)

# <input type="search" placeholder="Search for Vegetables and Fruits" class="search-keyword">
# driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
# driver.find_element(By.CSS_SELECTOR, "input[class='search-keyword']").send_keys("ber")
# driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
driver.find_element_by_xpath("//input[@class='search-keyword']").send_keys("ber")

# <button class="" type="button">ADD TO CART</button>
# "//button[text()='ADD TO CART']"
# //div[@class='product']/div/button
product_list = driver.find_elements_by_xpath("//div[@class='products']/div")
# assert len(product_list) == 3

add_to_cart_buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print(len(add_to_cart_buttons))
i = 0
# for button in add_to_cart_buttons:
#     if i < 3:
#         button.click()
#         time.sleep(2)
#         i+=1
#
#     else:
#         break
# time.sleep(4)
# add_to_cart_buttons[0].click()
add_to_cart_buttons[1].click()
# add_to_cart_buttons[2].click()

time.sleep(3)
# <img class=" " src="https://res.cloudinary.com/sivadass/image/upload/v1493548928/icons/bag.png" alt="Cart" xpath="1">
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
# <button type="button" class=" " xpath="1">PROCEED TO CHECKOUT</button>
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 5)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))
#
# # <input type="text" class="promoCode" placeholder="Enter promo code" xpath="1">
# driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
# # driver.find_element_by_class_name("promoCode").send_keys("coupon9999")
#
# # <button class="promoBtn" xpath="1">Apply</button>
# driver.find_element(By.XPATH, "//button[text()='Apply']").click()
#
#
# # <span class="promoInfo" style="color: green;" xpath="1">Code applied ..!</span>
# print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)
#
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
#
# # <button xpath="1">Place Order</button>
# driver.find_element_by_xpath("//button[text()='Place Order']").click()
time.sleep(2)
driver.close()