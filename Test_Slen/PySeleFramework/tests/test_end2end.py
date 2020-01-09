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

# pprint(grid[3])

"babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab"
"***bba**a*bbba**aab**b"
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def helper(s, p, si, pj, len_s, len_p):
            if si == len_s and pj == len_p:
                return True
            elif si == len_s:
                if p[pj] == '*':
                    return helper(s, p, si, pj + 1, len_s, len_p)
                else:
                    return False
            elif pj == len_p:
                if pj >= 1 and p[pj - 1] == '*':
                    return True
                else:
                    return False
            else:
                if s[si] == p[pj] or p[pj] == '?':
                    return helper(s, p, si + 1, pj + 1, len_s, len_p)
                elif p[pj] == '*':
                    return helper(s, p, si, pj + 1, len_s, len_p) or helper(s, p, si + 1, pj, len_s, len_p) or helper(s,
                                                                                                                      p,
                                                                                                                      si + 1,
                                                                                                                      pj + 1,
                                                                                                                      len_s,
                                                                                                                      len_p)
                else:
                    # return True  # typo
                    return False

        return helper(s, p, 0, 0, len(s), len(p))




