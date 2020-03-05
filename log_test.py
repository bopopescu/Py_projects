import os
import time
import subprocess
import shutil
import datetime
# test_master@jsun-mbpw10:~$ ssh ssqa@10.201.8.240
# helptell
#
# Last login: Mon Jan  6 17:33:23 2020 from 10.201.12.206
# locust --> performance Test
# Selenium Grid: cross browser testing
# mock
# Cassandra, ElasticSearch and Kafka, big data
# beautifulsoup, saucelabs
# Gatling, JMeter, and Locust are some load testing tools
# Swagger
# SoapUI or Apache JMeter
# Using SoapUI for load testing
# Testing SOAP/REST Web Services Using JMeter
# katalon API testing
# code profiler, code  refactor
# Selenium Grid
# Monitoring
# Mock
# locust : performance

#
##________________________________##

######______________________________________

#____________________________________________

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
from pprint import pprint
import  collections
from pandas import DataFrame
# print(DataFrame(rst))

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]
          ]
matrix1 = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
# [[-1,-1,2],[-1,0,1],[-1,1,0],[-1,2,-1],[0,1,-1]]
# [[-1,-1,2],[-1,0,1]]
#457
n = 5
for i in range(n,-1,-1):
    print(i, end=", ")
print(i)
for i in reversed(range(n+1)):
    print(i, end=", ")


# void rotate(vector<vector<int>>& matrix) {
#         int n = matrix.size();
#         for (int i = 0; i < n / 2; ++i) {
#             for (int j = i; j < n - 1 - i; ++j) {
#                 int tmp = matrix[i][j];
#                 matrix[i][j] = matrix[n - 1 - j][i];
#                 matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
#                 matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
#                 matrix[j][n - 1 - i] = tmp;
#             }
#         }
#     }

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


from collections import Counter
def min_num(A, B):
    cnt_max = 0
    dom_list = list(zip(A,B))
    top_list = sorted(dom_list, key= lambda arr: arr[0], reverse=True)
    bottom_list = sorted(dom_list, key = lambda arr: arr[1], reverse=True)










