from shutil import copy2, copy, copytree, copyfile
import os, glob
import fnmatch
import shutil
#os.path.exists will also return True if there's a regular file with that name.
#os.path.isdir will only return True if that path exists and is a directory.
#copy, copy2 need des. folder exists
#copy,copytree doesn't preserve meta data of copied files, copy2 does
py_file = glob.glob("*.py") # a list of .py files
if not os.path.exists("py_tmp"):
    os.mkdir("py_tmp")
for file in py_file:
    copy(file, "py_tmp")
if not os.path.exists("py_tmp"):
    copytree("py_tmp", "py_tmp_cptree")

#
#dir_src = ("C:\\foooo\\")
#dir_dst = ("C:\\toooo\\")

#for filename in os.listdir(dir_src):
#    if filename.endswith('.txt'):
#        shutil.copy( dir_src + filename, dir_dst)
#    print(filename)

temp = ""
for (root, dir, file) in os.walk(os.getcwd(), topdown = True):
    print("root   ->{}".format(root))
    print("dir    -> {}".format(dir))
    print("file   -> {}".format(file))
    print("root dirname  is {}".format(os.path.dirname(root)))
    print("root basename is {}".format(os.path.basename(root)))
    if root != temp:
        temp = root
        print("---------------------------------------------------------")


