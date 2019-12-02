import os
import time
import subprocess
import shutil
import datetime
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























cnt_list = []

for letter in cnt_dict.items():
    # print(letter, end=", ")
    cnt_list.append(letter)

cnt_order_list = sorted(cnt_list, key=lambda x: (x[1],x[0]), reverse=True)
# print(type(letter))
# print(f"cnt_list is {cnt_list}")
# print(f"cnt_order_list is {cnt_order_list}")
# print()



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
# 10_23

#*****
# ltr_str = "abcd"
# ltr_list = ltr_str.split("")
# print(ltr_list)

#
#
# use args, and kwargs
# str, built-in

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

##############################################

class Solution:
    def log_time(self, time: str) -> str:
        # Create time
        # size = 4, time_strList=[], tmp_str=''
        def time_gen(digit_chrSet, size, time_strList, tmp_str):
            if size == 0:
                time_strList.append(tmp_str)
                return
            else:
                for char in digit_chrSet:
                    # //improvement
                    time_gen(digit_chrSet, size - 1, time_strList, tmp_str + char)

        # save digits to a set

        loc_colon = 0
        digit_chrSet = set()
        for i, char in enumerate(time):
            if char == ':':
                loc_colon = i
            else:
                digit_chrSet.add(char)

        size = 4
        time_strList, tmp_str = [], ""

        time_gen(digit_chrSet, size, time_strList, tmp_str)

        min_time = float("inf")
        hr_st = int(time[0:loc_colon])
        min_st = int(time[loc_colon + 1:])
        time_strList_str = ""

        for time_str in time_strList:
            hrs = int(time_str[0:2])
            mins = int(time_str[2:])

            if hrs==hr_st  and mins == min_st:
                time_strList_str =   "00:00"
                break

            if hrs > 24 or mins > 59:
                continue
            else:
                if hr_st > hrs:
                    hr_diff = 24 - hr_st - 1 + hrs
                    min_diff = 60 - min_st + mins
                elif hr_st < hrs:
                    hr_diff = hrs - hr_st - 1
                    min_diff = 60 - min_st + mins
                else:

                    if mins >= min_st:
                        hr_diff = 0
                        min_diff = mins - min_st
                    else:
                        hr_diff = 23
                        min_diff = 59
                time_diff = hr_diff * 60 + min_diff

                if time_diff < min_time:
                    hrs_str = str(hrs) if hrs > 10 else '0' + str(hrs)
                
                    if mins < 10:
                        mins_str = '0' + str(mins)
                    else:
                        mins_str = str(mins)

                    time_strList_str = hrs_str + ":" + mins_str
                    min_time = time_diff

        return time_strList_str


