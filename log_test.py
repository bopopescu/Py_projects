import os
import time
import subprocess
import shutil
import datetime
import zipfile


def countSubstrings(self, s: str) -> int:
    size = len(s)

    queue = collections.deque((x, x) for x in range(size))

    for x in range(size - 1):
        if s[x] == s[x + 1]:
            queue.append((x, x + 1))
    ans = 0
    while queue:
        x, y = queue.popleft()
        ans += 1
        if x - 1 >= 0 and y + 1 < size and s[x - 1] == s[y + 1]:
            queue.append((x - 1, y + 1))
    return ans
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


###
def checkValidString(s: str) -> bool:
    def helper(start, size, q, s):
        if size == 0:
            if not q:
                return True
            else:
                return False

        else:
            if s[start] == '(':
                q.append('(')
                return helper(start + 1, size - 1, q, s)
            elif s[start] == ')':
                if not q:
                    return False
                else:
                    q.pop()
                    return helper(start + 1, size - 1, q, s)
            elif s[start] == '*':
                rst = helper(start + 1, size - 1, q[:], s)
                q.append('(')
                rst_left = helper(start + 1, size - 1, q[:], s)
                q.pop()
                rst_right = False
                if q:
                    q.pop()
                    rst_right = helper(start + 1, size - 1, q[:], s)
                return rst or rst_left or rst_right

    q = []
    start = 0
    size = len(s)
    return helper(start, size, q, s)

s = "(*))"
print(s)
print(checkValidString(s))



