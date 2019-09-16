from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time

class RunChromeTestWindows():
    def test(self):
        # driverLocaton = r"C:\Users\jsun\Documents\Py_projects\libs\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = driverLocaton
        # driver = webdriver.Chrome(driverLocaton)
        driver = webdriver.Chrome()
        #driver.get("http://www.letskodeit.com")
        driver.get("https://en.wikipedia.org")
        random_link = driver.find_element_by_id("n-randompage")
        time.sleep(3)

        # click "Random article"
        random_link.click()
        time.sleep(4)
        print(driver.title)

        driver.quit()



chromeTest = RunChromeTestWindows()
chromeTest.test()




