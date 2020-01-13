import os
import time
import subprocess
import shutil
import datetime

# pytest
# skip test: -m, -v, -k

# @pytest.mark.skip

# run selected testes @mark
# pytest -k 

# group tests
# @pytest.mark.Group_name
#pytest -m Group_name

# run except test
# pytest -m "not Group_name"
 
# execute setup b4 or after each test.
# @pytest.fixture(scope="module")
# def setup()
#     global driver
#     driver = webdriver.Chrome()
# Everything after yield executed after test is done 
    #   yield
    #   driver.close()

# def test_reg(setup):
#     pass

##________________________________##






import zipfile
from collections import Counter
cnt_dict = {'a':4, 'b':8, 'c':10, 'd':4, 'e':10, 'f':5, 'h':5, 'g':5}
chr_key  = cnt_dict.keys()
# print(next(chr_key))
# Traceback (most recent call last):
#   File "C:/Users/jsun/Documents/Py_projects/log_test.py", line 10, in <module>
#     print(next(chr_key))
# TypeError: 'dict_keys' object is not an iterator
key_iter = iter(chr_key)
print(next(key_iter)) # 'a'

import copy
S = 'abc'
shifts = [3,5,9]

# tmp = shifts[:]
tmp = copy.copy(shifts)
tmp[0] = 100
print(shifts)
print("****")

def shiftingLetters(S, shifts) -> str:
    rst = ""
    if len(S) < len(shifts):
        shifts = shifts[:len(S)]
    tmp_lst = shifts[:]
    tmp_lst[0] = 0
    print(f'shifts is {shifts}')

    for i in range(1, len(tmp_lst)):
        tmp_lst[i] = tmp_lst[i - 1] + shifts[i - 1]

    print(f'shifts is {shifts}')
    total = sum(shifts)
    print(f"total  is {total}")
    for i in range(len(tmp_lst)):
        tmp_lst[i] = total - tmp_lst[i]
        num = tmp_lst[i] + ord(S[i])
        if num <= ord('z'):
            rst += chr(num)
        else:
            num = (num - ord('z')) % 26
            rst += chr(ord('a') + num)

    if len(S) > len(shifts):
        rst += S[len(shifts):]

    return rst








##
# ————————————————

##

##
# install package
def install_pkg(package_loc, package_p_drive, package_name):
    # copy package fitime_strList
    package_to_copy = os.path.join(package_p_drive, package_name)
    shutil.copy2(package_to_copy, package_loc)

    for zip_file in os.listdir(package_loc):
        zip_file = os.path.join(package_loc, zip_file)
        try:
            with zipfile.ZipFile(zip_file, "r") as file:
                file.extractall(package_loc)
                setup_exe = os.path.join(package_loc, "IQfact_plus", "setup.exe")
                while True:
                    if os.path.isfile(setup_exe):
                        break
                    else:
                        time.sleep(1)
                install_pkg = subprocess.Popen([setup_exe, "/S"])
                install_pkg.wait()

        except zipfile.BadZipFile:
            print("Error: Zipfile is corrupted.")

    # clean up zip folder
    for files in os.listdir(package_loc):
        file_to_delete = os.path.join(package_loc, files)
        if os.path.isfile(file_to_delete):
            os.remove(file_to_delete)
        else:
            shutil.rmtree(file_to_delete)
# _________________________________________

# copy test flows to bin

def copy_flows(run_dir, flow_to_test, flowfile_loc, setupfile_loc):
    for flow_name in os.listdir(flowfile_loc):
        # flow_name = os.path.split(flow_name)[-1]
        flow_name = flow_name.split("\\")[-1]
        src = os.path.join(flowfile_loc, flow_name)
        shutil.copy2(src, run_dir)
        flow_to_test.append(flow_name)
    for setup_file in os.listdir(setupfile_loc):
        src = os.path.join(setupfile_loc, setup_file)
        shutil.copy2(src, run_dir)
print("start")

#*****
# 1170 , 8/29
# 9/25
# 10_23
# 12_9
# 1_10
class TestSolution:
    def numIs(self, grid):
        # 1/9/2020, 11:41
        # 1/10 8:17, 8:51

        def helper(grid, i, j, visited):

            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):

                if grid[i][j] == '0':
                    return True
                if visited[i][j]:
                    return True

                visited[i][j] = 1
                return helper(grid, i, j + 1, visited) and helper(grid, i + 1, j, visited) and helper(grid, i - 1, j,
                                                                                                      visited) and helper(
                    grid, i, j - 1, visited)
            return True

        if len(grid) == 0 or grid[0] == 0:
            return 0

        num_row, num_col = len(grid), len(grid[0])
        visited = [[0] * num_col for _ in range(num_row)]
        cnt = 0

        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j] == '0' or visited[i][j]:
                    continue
                if helper(grid, i, j, visited):
                    cnt += 1

        return cnt

class Solution:
    def numIs(self, grid):
        # 1/10 4:53 --> 5:05

        def helper(grid, i, j, visit):
            if i < 0 or i == len(grid) or j < 0 or j==len(grid[0]):
                return
            elif grid[i][j] == '0' or visit[i][j]  ==  1:
                return

            move = [(-1,0), (1,0), (0,-1), (0,1)]
            visit[i][j] = 1
            for m in move:
                helper(grid, i + m[0], j + m[1], visit)





        # return True or False

        row, col = len(grid), len(grid[0])
        if row == 0 or col == 0:
            return 0
        visit = [[0]*col for _ in range(row)]
        cnt = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0' or visit[i][j] == 1:
                    continue
                helper(grid, i, j, visit)
                cnt += 1

        return cnt

k = TestSolution()
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

print(f"k.numIs(grid) {k.numIs(grid)}")













##
import math
print(int(math.log2(8)) == math.log2(8) )
#_____________________________________________________________
#_______________________________________________________________
import os
cur_dir = os.path.abspath(__file__)
# print(cur_dir)
bb= os.path.dirname(cur_dir)
# print(os.path.dirname(cur_dir))
cc = os.path.dirname(bb)
# print(cc)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sss = [""]
# print("".join(sss))


