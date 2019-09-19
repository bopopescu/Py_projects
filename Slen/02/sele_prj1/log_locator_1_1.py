from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from log_locator_1 import WikipediaHomepage, WikipediaArticle
import os, time

class RunChromeTestWindows():
    def test(self):
        # driverLocaton = r"C:\Users\jsun\Documents\Py_projects\libs\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = driverLocaton
        # driver = webdriver.Chrome(driverLocaton)
        driver = webdriver.Chrome()
        driver.get("https://en.wikipedia.org")

        # random_link = driver.find_element_by_id("n-randompage")
        random_link = driver.find_element(*WikipediaHomepage.random_link) # use CSS_SELECTOR by ID
        random_link.click()
        time.sleep(3)

        # print random article's title from above
        first_heading = driver.find_element(*WikipediaArticle.first_heading)
        print(first_heading.text)
        time.sleep(2)

        # click on page information
        page_info = driver.find_element(*WikipediaArticle.page_info)
        page_info.click()
        time.sleep(3)

        # input in searchbox
        search_box = driver.find_element(*WikipediaArticle.search_box)
        search_box.send_keys("Selenium (Software)" + Keys.RETURN)
        time.sleep(3)

        # Xpath
        logo = driver.find_element(*WikipediaArticle.Logo)
        logo.click()
        time.sleep(3)
        
        driver.quit()





chromeTest = RunChromeTestWindows()
chromeTest.test()


 


 