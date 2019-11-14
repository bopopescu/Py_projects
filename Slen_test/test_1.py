from selenium import webdriver
import os

class RunChromeTestWindows():
    def test(self):
        driverLocaton = r"C:\Users\jsun\Documents\Py_projects\libs\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocaton
        driver = webdriver.Chrome(driverLocaton)
        driver.get("http://www.letskodeit.com")

chromeTest = RunChromeTestWindows()
chromeTest.test()




