from selenium import webdriver
from selenium.webdriver.common.by import By

import time
# ActionChains
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
url = "https://www.familysearch.org/"
driver.get(url)
driver.implicitly_wait(2)

action = ActionChains(driver)
# <a href="/search/" id="search" class="primary-nav-link" data-test="header-mainnav-search" data-config="lo_hdr_srch"
# role="button" aria-haspopup="true" aria-expanded="false" aria-controls="search-submenu" aria-owns="search-submenu"
# data-component-init="AdobeLinkTracker">Search</a>
action_item = action.move_to_element(driver.find_element(By.ID, "search"))
# action_item.perform()
# <a href="/search/family-trees" class="sub-menu-link" data-config="lo_hdr_srch:genealogies" data-test="genealogies"
# data-component-init="AdobeLinkTracker">Genealogies</a>
action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()

# <h1 class="grande fs-h3">Search Genealogies</h1>
# text_ver = driver.find_element_by_xpath("//h1[text()='Search Genealogies']").text # working
# text_ver = driver.find_element(By.XPATH, "//div[@class='search-purpose']/h1").text
text_ver = driver.find_element(By.CSS_SELECTOR, "div[class='search-purpose'] h1").text
print(text_ver) # Search Genealogies


# ex1
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(executable_path="")
driver.get("https://UrlToOpen")

action = ActionChains(driver)

firstLevelMenu = driver.find_element_by_id("menu")
action.move_to_element(firstLevelMenu).perform()

secondLevelMenu = driver.find_element_by_xpath("//a[contains(text(),'menu1')]")
action.move_to_element(secondLevelMenu).perform()
secondLevelMenu.click()





time.sleep(3)
driver.close()