
from shutil import copyfile, copy2 #copytree
import os
import shutil
from pathlib import Path
import errno



"""
path = (os.getcwd()) + "\\test_folder"
if Path(path).exists(): # exists check if a file or a path exist
    print("{} exists".format(path))
if os.path.isdir(path):
    print("delete path successful")
    shutil.rmtree(path) # remove dir and its contents
if not Path(path).exists(): #os.path.exists(file_path)
    print("{} does not exist".format(path))
    os.mkdir(path)
    #shutil.rmtree(path)
#if not os.path.exists(directory):
#   os.makedirs(directory)
"""

#filename = "doc_dir1\\doc_dir2\\doc_dir.txt"
#filename = "doc_dir1/doc_dir2/doc_dir.txt"
filename = os.path.join("doc_dir1", "doc_dir2", "doc_dir.txt")
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename),exist_ok = True)
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

print(os.path.dirname(filename))

#mkdir , create single sub-directory
#makedirs, create all the intermediate directory
#In Python3, os.makedirs has a default parameter exist_ok=False.
#If you set it to True, then os.makedirs will not throw any exception
# if the leaf exists.


# os.mkdir vs os.makedirs
#os.makedirs makes all the directories, so if I type in shell (and get nothing):
#new_dir = os.path.join(os.getcwd(),"mkdir")
#os.path.join(os.sep, 'home', 'build', 'test', 'sandboxes', todaystr, 'new_sandbox')
new_dir1 = os.path.join(os.getcwd(),"makedirs\\new_dir")
shutil.rmtree("makedirs")
os.makedirs(new_dir1) # os.mkdir(new_dir1) --> error

