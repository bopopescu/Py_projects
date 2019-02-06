from shutil import copyfile, copy2
import os
import shutil
from pathlib import Path


from shutil import copyfile, copy2 #copytree
import os
import shutil
from pathlib import Path




"""
By design, rmtree fails on folder trees containing read-only files. 
If you want the folder to be deleted regardless of whether 
it contains read-only files, then use
shutil.rmtree('/folder_name', ignore_errors=True)
"""
with open("doc_dir.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
with open("doc_dir.txt","r") as ins:
    x = [ l.strip() for l in ins]
with open("doc_dir.txt") as f:
    content = f.readlines()
"""
Note that this approach has 2 downsides:
1) You store all the lines in memory. In the general case, this is a very bad idea. 
The file could be very large, and you could run out of memory. Even if it's not large, it is simply a waste of memory.
2) This does not allow processing of each line as you read them. 
So if you process your lines after this, it is not efficient (requires two passes rather than one).
"""

with open("doc_dir.txt") as f:
    content = f.read().splitlines()
# list all files in a dir
# os.listdir()

onlyfiles = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(),f))]
#print(onlyfiles)
onlyfiles = [ f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]
print(onlyfiles)
#for f in os.listdir(os.getcwd()):
    #print(f)# pirnt out files or dirs in relative path
import glob
py_file = glob.glob("*.py")
print(py_file)
file_abspath = [os.path.abspath(f) for f in os.listdir()]
print(file_abspath)

old_list = [1,2,3]
new_list = old_list

new_list.append(5)
print(old_list)


