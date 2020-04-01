from selenium import webdriver
import os
import time
class FindByXpathCss():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementByXpath  = driver.find_element_by_xpath("//input[@id='name']")

        if elementByXpath is not None:
            print("Found an element by XPATH")
        # < input
        # id = "displayed-text"
        # name = "show-hide"
        # class ="inputs displayed-class" placeholder="Hide/Show Example" type="text" >
        elementByCss = driver.find_element_by_css_selector("#displayed-text")
        if elementByCss:
            print("Found an element by CSS")

ff = FindByXpathCss()
ff.test()

time.sleep(199)






