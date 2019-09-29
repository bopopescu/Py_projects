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
string = '   xoxo love xoxo    '
# print("string is {}, len is {}".format(string, len(string)))
# string is    xoxo love xoxo    , len is 21

str1 = string.strip()
#removed 3 leading spaces and 4 trailing spaces
# print("str1 is {}, len is {}".format(str1, len(str1)))
# str1 is xoxo love xoxo, len is 14

str2= string.strip('xoxo')
# # Nothing is removed
print("str2 is {}, len is {}".format(str2, len(str2)))
# # str2 is    xoxo love xoxo    , len is 21

str3= string.strip(' xoxo')
# #
print("str3 is {}, len is {}".format(str3, len(str3)))
# # str3 is love, len is 4



#
# # Argument doesn't contain space
# # No characters are removed.
# print(string.strip('sti'))
#
# string = 'android is awesome'
# print(string.strip('an'))

#assert 1+1 == 3, "True"
# __________________________________________

#___________________________________________
#*****
# run test flows
#
#






