from selenium import webdriver
import os, time

class RunChromeTestWindows():
    def test(self):
        # driverLocaton = r"C:\Users\jsun\Documents\Py_projects\libs\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = driverLocaton
        # driver = webdriver.Chrome(driverLocaton)

        driver = webdriver.Chrome()

        driver.get("http://www.letskodeit.com")
        # driver.get("http://www.yahoo.com")
        time.sleep(10)
        driver.close()



chromeTest = RunChromeTestWindows()
chromeTest.test()




