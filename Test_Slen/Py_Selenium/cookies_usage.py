from selenium import webdriver
driver= webdriver.Chrome()

# Get Cookies in python
# get_cookies() used to return the list of all cookies stored in the web browser.

# Go to the correct domain
driver.get("https://www.example.com")
# And now output all the available cookies for the current URL
driver.get_cookies()

# Get Cookie by name in python selenium
# get_cookie() used to return the specific cookie according to its name.
driver.get_cookie('foo')

# Add Cookie in python selenium
# add_cookie() method is used to create and add the cookie.
# Go to the correct domain
driver.get("https://chercher.tech")
# Now set the cookie. This one's valid for the entire domain
cookie = {'name' : 'foo', 'value' : 'bar'}
driver.add_cookie(cookie)


# Delete Cookie in python
# Using delete_cookie() to delete a cookie according to its name.

driver.delete_cookie("foo")

# Delete All Cookie in python selenium
# delete_all_cookies() is used to delete all cookies.
driver.delete_all_cookies()

# _______________________________________________________________________
"""
Suppose we have to test for the following scenario:

1. Go to login page and login to the application
2. Close the browser
3. Open the browser and go to the login page - the user should not see the login form and should be already logged in.

On the first login, cookies are stored in the browser. In WebDriver, when the browser window is closed, 
all session data and cookies are deleted, so the testing of the above scenario becomes impossible.

Luckily, WebDriver has functionality to read the cookies from the browser before closing it and 
then restore the cookies in the new browser window.
"""

package com.testingexcellence.webdriver;
import org.openqa.selenium.By;
import org.openqa.selenium.Cookie;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.Assert;

import java.util.Set;

public class CookieTest {
    WebDriver driver;

    @Test
    public void login_state_should_be_restored() {
        driver = new FirefoxDriver();

        driver.get("http://www.example.com/login");
        driver.findElement(By.id("username")).sendKeys("admin");
        driver.findElement(By.id("password")).sendKeys("12345");
        driver.findElement(By.id("login")).click();

        Assert.assertTrue(
                driver.findElement(By.id("welcome")).isDisplayed());

        //Before closing the browser, read the cookies
        Set allCookies = driver.manage().getCookies();

        driver.close();

        //open a new browser window
        driver = new FirefoxDriver();

        //restore all cookies from previous session
        for(Cookie cookie : allCookies) {
            driver.manage().addCookie(cookie);
        }

        driver.get("http://www.example.com/login");

//Login page should not be disaplyed
        Assert.assertTrue(
                driver.findElement(By.id("welcome")).isDisplayed());

        driver.close();
    }
}

#


