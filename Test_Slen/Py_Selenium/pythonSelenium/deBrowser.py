from selenium import webdriver
import time
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
# driver = webdriver.Ie()
driver.get("http://www.litepoint.com")
time.sleep(2)
print(driver.title)
print(driver.current_url)
# driver.close() # close current window
# driver.quit() # close all windows
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
time.sleep(5)
driver.back()
driver.refresh()
driver.minimize_window()
time.sleep(3)

driver.close()


# time.sleep(5)
