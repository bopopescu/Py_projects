from shutil import copyfile, copy2 #copytree
import os
import shutil
from pathlib import Path
import errno
import glob
"""
py_file = glob.glob("*.py")
print(py_file)

old_list = [1,2,3]
new_list = old_list

new_list.append(5)
print(old_list)

path = "file_log.py"
if Path(path).exists():
    os.remove(path)
    print("works")
path = glob.glob("*.txt")
print(path)
#os.remove(path[0])
print(glob.glob("*.txt"))

with open("doc_dir_cpy.txt","r") as fin:
    content = fin.readlines()
    print(type(content))
    print(content)
    #print("this is bll")
    #print(["this ","is","ok"])
    
"""
log_name = "doc_dir_cpy.txt"
fpath = os.path.abspath(log_name) #full path include file name
print("fpath {}".format(fpath))
print(type(fpath))

(f_path, file_name) = os.path.split(fpath)
print("f_path-->{}, file_name-->{} ".format(f_path,file_name) )
a = os.listdir(f_path)

#fpath C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\unzipped_content\doc_dir_cpy.txt
#f_path-->C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\unzipped_content, file_name-->doc_dir_cpy.txt

abs_path = "C:\\Users\\jsun\\Documents\\pyProjects\\Auto_Jenkins\\unzipped_content"
print(os.path.abspath(abs_path))
#"C:\\Users\\jsun\\Documents\\pyProjects\\Auto_Jenkins\\unzipped_content"

b = glob.glob(f_path + '\\*.py')
sub_folder = "C:\\Users\\jsun\\Documents\\pyProjects\\Auto_Jenkins\\unzipped_content\\**\\*.csv"
sub_folder_sch = glob.glob(sub_folder, recursive=True)
print(sub_folder_sch)

##
from shutil import copyfile, copy2 #copytree
import os
import shutil
from pathlib import Path
import errno
import glob

file_delete = glob.glob(os.path.join(os.getcwd(),"log_test.txt"))
print(file_delete)


if os.path.isfile(file_delete[0]):
    print(file_delete[0])
    print((os.path.split(file_delete[0])))
    #('C:\\Users\\jsun\\Documents\\pyProjects\\Auto_Jenkins\\unzipped_content', 'log_test.txt')
    #print(os.listdir((file_delete[0].split())[0]))
    #os.remove(file_delete[0])
else:
    print("dir")
"""
To find files in immediate subdirectories:

configfiles = glob.glob(r'C:\Users\sam\Desktop\*\*.txt')
For a recursive version that traverse all subdirectories, you could use ** and pass recursive=True since Python 3.5:

configfiles = glob.glob(r'C:\Users\sam\Desktop\**\*.txt', recursive=True)
"""

in_file = "output_file1.txt"
with open(in_file,"r") as fin:
    ori=[]
    chan=[]
    for i in fin:
        ori.append(i)
        line = i.strip().lower()# strip a string out of white space, lower is to whole string
        chan.append(line)
        #print("*******************")
    print(ori)
    print("*****")
    print(chan)