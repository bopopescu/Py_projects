import pytest
import time



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestOne:

    def test_e2e(self, setup):
        pass

from pprint import pprint
grid = [[[0] * 5 for y in range(4)] for z in range(3)]

pprint(grid[3])