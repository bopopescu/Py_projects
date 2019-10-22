import os
import time
import subprocess
import shutil
import datetime
import zipfile


# install package
def install_pkg(package_loc, package_p_drive, package_name):
    # copy package first
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


#__________________________________________
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

from statistics import mean
a = [1,2]
print(f"mean(a) is {mean(a)}")


def countAndSay(n: int) -> str:
    rst = "1"
    if n == 1:
        return '1'

    while n > 1:

        i = 0
        rst_new = ""
        while i < len(rst):
            cnt = 1
            tmp = rst[i]
            if i + 1 == len(rst) or rst[i + 1] != rst[i]:
                i += 1
            else:
                while i + 1 < len(rst) and rst[i + 1] == rst[i]:
                    i += 1
                    cnt += 1

            rst_new += str(cnt) + tmp
        rst = rst_new
        n -= 1

    return rst

print(f"countAndSay is {countAndSay(3)}")


def countAndSay(self, n: int) -> str:
    rst = "1"
    if n == 1:
        return '1'

    while n > 1:

        i = 0
        rst_new = ""

        while i < len(rst):
            cnt = 1
            j = i
            while j + 1 < len(rst) and rst[j + 1] == rst[i]:
                cnt += 1
                j += 1

            rst_new += str(cnt) + rst[i]
            if j == i:
                i += 1
            else:
                i = j
        rst = rst_new
        n -= 1
    return rst
for i in range(10):
    if i == 0:
        i = 9
    print(i, end=", ")
#_
1.     1
2.     11
3.     21
4.     1211
5.     111221__________________________________________
#*****
# run test flows
#
#
# use args, and kwargs
# str, built-in

import os
cur_dir = os.path.abspath(__file__)
print(cur_dir)
bb= os.path.dirname(cur_dir)
print(os.path.dirname(cur_dir))
cc = os.path.dirname(bb)
print(cc)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




