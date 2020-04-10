from selenium import webdriver
dr = webdriver.Chrome()

url = 'www.yahoo.com'
dr.get(url)

dr.get_cookies()

dr.delete_all_cookies()

dr.add_cookie()
