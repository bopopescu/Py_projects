from selenium import webdriver
import os
import time
class FindByTagClass():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        # < input
        # id = "displayed-text"
        # name = "show-hide"
        # class ="inputs displayed-class" placeholder="Hide/Show Example" type="text" >
        elementByClassName  = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Run test")

        print(elementByClassName.get_attribute("value"))
        print(elementByClassName.get_attribute("class"))

        if elementByClassName is not None:
            print("Found an element by Class Name")

        elementByTagName = driver.find_element_by_tag_name("a")
        if elementByTagName:
            print("Found an element by TagName")

        time.sleep(10)
        driver.close()

ff = FindByTagClass()
ff.test()





