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
# 10_23

#*****
# ltr_str = "abcd"
# ltr_list = ltr_str.split("")
# print(ltr_list)

def pair_team(teams):
    if len(teams) == 1:
        return teams[0]

    new_team = []
    i, j = 0, len(teams) - 1

    while i < j:
        new_team.append('(' + teams[i] + ',' + teams[j] + ')')
        i += 1
        j -= 1

    return pair_team(new_team)

n=8
teams = [str(i) for i in range(1, n + 1)]
print(teams)
print(pair_team(teams))
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

sss = [""]
print("".join(sss))


