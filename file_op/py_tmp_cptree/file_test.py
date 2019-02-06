from shutil import copy2, copy, copytree,copyfile
import os, glob
#copy, copy2 need des. folder exists
#copy doesn't preserve meta data of copied files, copy2 does
py_file = glob.glob("*.py") # a list of .py files
if not os.path.exists("py_tmp"):
    os.mkdir("py_tmp")
for file in py_file:
    copy(file, "py_tmp")
copytree("py_tmp", "py_tmp_cptree")


