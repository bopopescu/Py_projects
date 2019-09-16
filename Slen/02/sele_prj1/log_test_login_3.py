from selenium import webdriver
from log_login_3 import LoginPage
import unittest


class LoginTestCase(unittest.TestCase):


    def testUserLogin(self):
        self.login_page = LoginPage()
        user = "jsun"
        password = "1234"
        self.login_page.log_in_as(user, password)
        welcome_message = self.login_page.get_auth_message()
        self.assertIn("Welcome back", welcome_message.text)

    def testLoginFail(self):
        self.login_page = LoginPage()
        user = "jsun"
        password = "12345"
        self.login_page.log_in_as(user, password)
        message = self.login_page.get_auth_message()
        self.assertIn("Account not found", message.text)
        self.login_page.click_register_link()
        header = self.login_page.get_page_header()
        self.assertIn("Create an Account", header.text)

if __name__ == "__main__":
    unittest.main(verbosity=2)
    
        











class LoginPage(Browser):
    def __init__(self):
        self.LOGIN = '/'
    
    def log_in_as(self, username, password):
        self.visit(self.LOGIN)
        username_field = self.find_element(*LoginPageLocators.username_field)
        password_field = self.find_element(*LoginPageLocator.password_field)
        submit_btn     = self.find_element(*LoginPageLocators.submit_btn)
        username_field.send_keys(username)
        password_field.send_keys(password)
        submit_btn.click()
        time.sleep(3)
    
    def get_auth_message(self):
        return self.find_element(*LoginPageLocators.message)

    def click_register_link(self):
        create_account_link = self.find_element(*LoginPageLocators.create_acct_link)
        create_account_link.click()
        time.sleep(3)

    def get_page_header(self):
        return self.find_element(*CreateAccountPageLocators.header)
    


