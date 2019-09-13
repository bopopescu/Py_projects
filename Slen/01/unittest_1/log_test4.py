from selenium import webdriver
import os
import time
class FindByTagClass():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementByClassName  = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Run test")

        if elementByClassName is not None:
            print("Found an element by Class Name")

        elementByTagName = driver.find_element_by_tag_name("a")
        if elementByTagName:
            print("Found an element by TagName")

ff = FindByTagClass()
ff.test()

time.sleep(199)




