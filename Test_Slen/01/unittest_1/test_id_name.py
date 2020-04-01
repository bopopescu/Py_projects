from selenium import webdriver
import os
import time
class FindByIdName():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementById  = driver.find_element_by_id("name")

        if elementById is not None:
            print("Found an element by Id")

        elementByName = driver.find_element_by_name("show-hide")
        if elementByName:
            print("Found an element by Name")

ff = FindByIdName()
ff.test()

time.sleep(199)


#
  

