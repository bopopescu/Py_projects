from shutil import copy2, copy, copytree, copyfile
import os, glob
import fnmatch
import shutil



#os.path.exists will also return True if there's a regular file with that name.
#os.path.isdir will only return True if that path exists and is a directory.

# copy, copy2 need des. folder exists
# if file exists, copy2 will overwirte the file with same name
# copy,copytree doesn't preserve meta data of copied files, copy2 does
# os.remove(file_name)
import shutil
import os
############

#########


print(os.getcwd())
#os.remove("write_log.txt")

# os.path.join(path, *paths)
#src = os.path.join(os.getcwd(), "zip_op", "write_log.txt")
#src = r".\zip_op\wriet_log.txt"
#src = os.path.join( "zip_op", "write_log.txt")
#src = "zip_op\\write_log.txt"
src = ".\zip_op\write_log.txt"
#des = "."
des = "write_log.txt"
shutil.copy2(src, des)

#_____________________________________________________
py_file = glob.glob("*.py") # a list of .py files
# ['manage.py']



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


#
#os.path.split(path) split the pathname path into a pair; (head, tail).

#os.path.dirname(path) returns the head of the path.
#The dirname of '/foo/bar/item' is '/foo/bar'.

#os.path.basename(path) returns the tail of the path.
# The basename of '/foo/bar/item' returns 'item'

import shutil
import os

for i in os.listdir("."):
    print(i, os.path.basename(os.path.abspath(i)), os.path.dirname(os.path.abspath(i)), sep=", ")

# find file size

def getFilesize(file):
    with open(file,"r") as f:
        f.seek(0, os.SEEK_END)# os.SEEK_SET, os.SEEK_CUR
        #fstream = open(file, 'r')
        #fstream.seek(0, os.SEEK_END)
        FILE_SIZE = f.tell()
        return FILE_SIZE

if __name__  == "__main__":
    import os
    print("file size is ", os.path.getsize(__file__))
    print("file size is ", os.stat(__file__).st_size)
    print(getFilesize(__file__))
#rename directory
import os

for dirs in os.listdir(os.getcwd()):
    if os.path.isdir(dirs):
        dirs_replace = dirs.replace("Chapter", "result_log")
        print(dirs_replace)
        os.rename(dirs, dirs_replace)

#
# ch4/example1.py
import os, shutil
n_files = 10
files = []

# method 1
file_dir = "output2"
if os.path.isdir(file_dir):
    shutil.rmtree(file_dir)
os.mkdir(file_dir)
file_descriptor = []
for i in range(n_files):
    file = os.path.join(file_dir, "logall{}.txt".format(i))
    t= open(file, 'w')
    file_descriptor.append(t)

line = 0
for i in file_descriptor:
    print(line, i, sep="-")
    line += 1

# method 2
'''for i in range(n_files):
    f = open('output1/sample%i.txt' % i, 'w')
    files.append(f)
    f.close()'''

# method 3
'''for i in range(n_files):
    with open('output1/sample%i.txt' % i, 'w') as f:
        files.append(f)'''

import subprocess

cmd = ['ping', '127.0.0.1', '-n', '5']
exec = subprocess.Popen(cmd, stdout=subprocess.PIPE)
exec.wait()
print("done")
for line in exec.stdout:
    print(line.decode('utf-8').strip())
    print(line)

#
import subprocess

p1 = subprocess.Popen('dir', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p2 = subprocess.Popen('sort /R', shell=True, stdin=p1.stdout)

p1.stdout.close()
out, err = p2.communicate()

##
print('read:')
proc = subprocess.Popen(
    ['echo', '"to stdout"'],
    stdout=subprocess.PIPE,
)
stdout_value = proc.communicate()[0].decode('utf-8')
print('stdout:', repr(stdout_value))

import os
base = os.path.abspath(__file__)
print(base)
a= os.path.dirname(base)
b = os.path.dirname(a)
print(a,b,sep=", ")
