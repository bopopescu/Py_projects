from selenium import webdriver
import time

# locator actions
# send_keys("content"), click(), text,clear()
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
url = "https://login.salesforce.com"
# url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
time.sleep(1)
print(driver.title)
print(driver.current_url)
driver.find_element_by_css_selector("#username").send_keys("ssqa")
driver.find_element_by_css_selector(".password").send_keys("ssqa")
time.sleep(2)
driver.find_element_by_css_selector(".password").clear()
time.sleep(2)
#@@ locator: link_text
driver.find_element_by_link_text("Forgot Your Password?").click()
time.sleep(3)

#@@ 1. Generate css from class name
# tagname.class_name
# make sure no space in class name, replace space with .

#@@ 2. Generate xpath based on text, text is case-sensitive
# //tagname[text()='xxx']
# driver.find_element_by_xpath("//a[text()='cancel']").click()
# "cancel" Should be "Cancel"
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//a[text()='cancel']"}
driver.find_element_by_xpath("//a[text()='Cancel']").click()
time.sleep(3)

#@@3. Create Xpath and CSS by Traversing Tags
# xpath: ParentTag/ChildTag
# css:   ParentTag ChildTag

#@@4. Select Parent Locator from Child using Xpath
# Xpath/parent::tagName

driver.close()



























































































class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def if_predecessor(w1, w2):
            if len(w1) + 1 != len(w2):
                return False
            cnt = 0
            i, j = 0, 0
            while i < len(w1) and j < len(w2):
                if w1[i] != w2[j]:
                    cnt += 1
                    if cnt > 1:
                        return False
                else:
                    i += 1
                j += 1
            return True

        dp = [1] * len(words)
        cnt_max = 1

        words = sorted(words, key=len)
        for i in range(1, len(words)):
            for j in range(i):
                if if_predecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    cnt_max = dp[i] if cnt_max < dp[i] else cnt_max

        return cnt_max

    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        words.sort(key=len)
        dp = collections.defaultdict(int)
        result = 0
        for word in words:
            for index in range(len(word)):
                char_excluded_string = word[:index] + word[index + 1:]
                if char_excluded_string in dp:
                    dp[word] = max(dp[char_excluded_string] + 1, dp[word])
                else:
                    dp[word] = max(dp[word], 1)
            result = max(dp[word], result)
        return result


def longestStrChain(self, words: List[str]) -> int:
    """
    :type words: List[str]
    :rtype: int
    """

    def isPredecessor(s1, s2):
        add = False
        s1_inx = 0
        s2_inx = 0
        while s1_inx < len(s1) and s2_inx < len(s2):
            if s1[s1_inx] == s2[s2_inx]:
                s1_inx += 1
                s2_inx += 1
            elif add == False:
                s2_inx += 1
                add = True
            else:
                return False
        return True

    words = sorted(words, key=len)
    dp = [1] * len(words)
    res = 1
    for i in range(len(words)):
        for j in range(0, i):
            if len(words[i]) == len(words[j]):
                break
            elif len(words[i]) - 1 > len(words[j]):
                continue
            else:
                if isPredecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])
    # print words
    # print dp
    return res