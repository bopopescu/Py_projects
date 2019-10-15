from selenium.webdriver.common.by import By

class LoginPage():
    username_field = (By.CSS_SELECTOR, "#username")
    password_field = (By.CSS_SELECTOR, "#password")
    submit_btn     = (By.NAME, 'submit')
    create_acct_link = (By.LINK_TEXT, 'Create an account')
    message = (By.CSS_SELECTOR, "#auth-message")

class CreateAccountPage():
    header = (By.CSS_SELECTOR, "#header")