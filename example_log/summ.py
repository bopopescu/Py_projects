"""
os.path.split()
os.path.isfile()
os.path.abspath()
str.split()
list_local.append()
list_local.extend()


"""
data1 = list(range(0, 1000, 3))
data2 = list(range(0, 1000, 5))
data3 = list(set(data1 + data2)) # makes new list without duplicates
total = sum(data3) # calculate sum of data3 list's elements
print (total)
print(type(range(10))) # <class 'range'>, not list, cant add two ranges
# copying a list
#new_list = list.copy()
#abspath vs realpath
#os.path.exists vs os.path.isdir
"""
os.path.abspath returns the absolute path, but does NOT resolve symlinks.
os.path.realpath will first resolve any symbolic links in the path, and then return the absolute path.
"""
# Adding element to the new list
a = [i for i in range(10)]
print (type(a))
print (a)

# str.split(" ")
line="a sentence with a few words"
line_list = line.split() # ['a', 'sentence', 'with', 'a', 'few', 'words']
#
qa = "routine QA auto on Mac. and other sta. cases"
#wo = qa.split()
import string
wo = [word.strip(string.punctuation) for word in qa.split()]

path, filename = os.path.split("QA_Auto.py")
filename = os.path.splitext(filename)[0]
newfilename = 'ok_%s.txt' % filename
newpath = os.path.join(path, newfilename)
os.path.join(os.path.sep, 'home','build','test','sandboxes',todaystr,'new_sandbox')
##

"""
* read(size) >> size is an optional numeric argument and this func returns a quantity of 
*data equal to size. If size if omitted, then it reads the entire file and returns it

* readline() >> reads a single line from file with newline at the end

* readlines() >> returns a list containing all the lines in the file

* xreadlines() >> Returns a generator to loop over every single line in the file
"""
file_name = "fun1.py"
"""
with open(file_name) as f:
    lines = f.readlines()
for line in lines:
    print(line,end="")
# without "\n"
#f.read().splitlines()
"""
def readlines():
    with open("sorted_output.txt") as f:
        line = f.readlines()

def readline():
    with open("sorted_output.txt") as f:
        line = f.readline()
        lines = []
        while line:
            lines.append(line)
            line = f.readline()

def iterate():
    with open("sorted_output.txt") as f:
        lines = []
        for line in f:
            lines.append(line)

def comprehension():
    with open("sorted_output.txt") as f:
        lines = [line for line in f]
import os.path
import glob

fpath=os.path.abspath('fun2.py')
(f_path,filename)=os.path.split(fpath)
print(f_path)
a=os.listdir(f_path)

for line in a:
    print(line)
print()
print("done os.listdir()")
b=glob.glob(f_path+'\\*.py')
for line in b:
    print(line)
"""
C:\Users\jsun\Documents\pyProjects\Auto_Jenkins
.idea
cla1.py
extracted_folder
extracted_folder1
ex_2.py
fun1.py
fun2.py
IQfact+_BRCM_4364_MPS_3.4.1.17
IQfact+_BRCM_4364_MPS_3.4.1.17.zip
QA_Auto.py
Run_Pkg_Installation.py
Run_Pkg_Installation_test.py
Run_QA.py
summ.py
test.py
test1.py
Verify.py
Verify_IQfact+_MRVL_8801
write.zip
write1.zip
__pycache__

done os.listdir()
C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\cla1.py
C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\ex_2.py
C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\fun1.py
C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\fun2.py
C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\QA_Auto.py
C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\Run_Pkg_Installation.py
C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\Run_Pkg_Installation_test.py
C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\Run_QA.py
C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\summ.py
C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\test.py
C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\test1.py
C:\Users\jsun\Documents\pyProjects\Auto_Jenkins\Verify.py

Process finished with exit code 0
 
"""
"""
print()
text_lines= [text_line.rstrip() for text_line in open(file_name)]
for line in text_lines:
     print(line,end="")
"""
"""
with open("file.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
"""
"""
#copy files
from shutil import copyfile
import os.path
src = "fun2.py"
dst = "copy_of_fun2.py"
copyfile(src, dst)
if os.path.isfile(dst):
    print(dst, "exists")


"""
"""
import os
import shutil
import tempfile

shutil.copy (filename1, filename2)

os.mkdir (dirname1)
shutil.copytree (dirname1, dirname2)

import os
import os.path
import shutil
import subprocess

import zipfile
import glob
import time

pkg_name = "IQfact+_BRCM_4364_MPS_3.4.1.17"#\\IQfact_plus"
dir_cur = os.getcwd() #str
dir_pkg = os.path.join(dir_cur,pkg_name)
print (dir_pkg)
print (os.listdir(dir_pkg))
os.chdir(dir_pkg)
setup_exe = glob.glob("S*.exe")
print (type(setup_exe),"-->", setup_exe)
from pywinauto.application import Application
app = Application().start("setup.exe")
#app.IQfact_plusInstallation.Cancel.click()
#app.userAccountControl.Yes.click()
app.IQfact_plusInstallation.InstallSelectedItems.click()
app.userAccountControl.Yes.click()
app.userAccountControl.Yes.click()
app.MicrosoftVisual.Next.click()
os.system("pause")
#subprocess.run([setup_exe[0],"-Install Selected Items"], shell = True)

"""

"""
from pywinauto.application import Application
# Run a target application
app = Application().start("notepad.exe")
# Select a menu item
app.UntitledNotepad.menu_select("Help->About Notepad")
# Click on a button
app.AboutNotepad.OK.click()
# Type a text string
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
"""
os.system('cp nameoffilegeneratedbyprogram /otherdirectory/')
os.system('cp '+ rawfile + ' rawdata.dat')
"""
output = file_name
for line in open("file.txt", "r"):
    list.append(line)
    if len(list) == 1000000:
        output.writelines(list)
        del list[:]

#
#
#
import shutil
shutil.copy('/etc/hostname', '/var/tmp/testhostname')
#shutil.copy(filePath, folderPath)

"""
#copy text from one file to another
inputFile = open("Input.txt","r")
text = inputFile.read()
inputFile.close()
outputFile = open("Output.txt","w")
outputFile.write(text)
outputFile.close()

#open input file and read all lines and save it in a list
fin = open("Input.txt","r")
f = fin.readlines()
fin.close()

#open output file and write all lines in it
fout = open("Output.txt","wt")
for i in f:
    fout.write(i)
fout.close()

import shutil
shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext') # complete target filename given
shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext
"""
if not os.path.exists(directory): #race condition is possible
    os.makedirs(directory)

import os
import errno

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

print("{1}...{0} appears {2} times.".format(1,'b',3.14))
#b...1 appears 3.14 times.

os.path.join("c:\\", "\\home", "foo", "bar", "some.txt")
'c:\\home\\foo\\bar\\some.txt'

os.path.join("\\c:\\", "\\home", "foo", "bar", "some.txt")
'\\home\\foo\\bar\\some.txt'

os.path.join("\\c:\\", "home", "foo", "bar", "some.txt")
'\\c:\\home\\foo\\bar\\some.txt'

os.path.join("\\c:\\", "home", "foo", "\\bar", "some.txt")
'\\bar\\some.txt'

#
import os.path
b = os.path.abspath('') #return current working path
print ('b is ',b)
print(type(b))
#b is  C:\Users\jsun\Documents\pyProjects\Auto_Jenkins
#<class 'str'>

#
c = os.path.basename('\\c:\\home\\foo\\bar\\some.txt')
print ("c is ", c)
c is  some.txt
<class 'str'>
#
c = os.path.basename('\\c:\\home\\foo\\bar')
c is  bar
#
d = os.path.dirname('\\c:\\home\\foo\\bar\\some.txt')
print (d)  #\c:\home\foo\bar
print (type(d)) # <class 'str'>
#
d = os.path.dirname('\\c:\\home\\foo\\bar')
print (d)  #\c:\home\foo
print (type(d)) # <class 'str'>
#
d = os.path.exists('\\c:\\home\\foo\\bar\\')
print (d)  # False
print (type(d)) # <class 'bool'>
#
d = os.path.isfile('C:\\Users\\jsun\\Documents\\pyProjects\\Auto_Jenkins\\fun1.py')
print (d)  # True
print (type(d)) # <class 'bool'>
#
d = os.path.isdir('C:\\Users\\jsun\\Documents\\pyProjects')
print (d)  # True
print (type(d)) # <class 'bool'>
#
dd = os.path.split("C:\\Users\\jsun\\Documents\\test.txt")
print (type(dd))
dd is  ('C:\\Users\\jsun\\Documents', 'test.txt')
<class 'tuple'>


dd = os.path.split("C:\\Users\\jsun\\Documents")
('C:\\Users\\jsun', 'Documents')
dd = os.path.split("C:\\Users\\jsun\\Documents\\")
dd is  ('C:\\Users\\jsun\\Documents', '')
"""
import os.path
import zipfile

with zipfile.ZipFile('log_all.zip',"w") as zf:
    file_list = ['Run_QA.py','doc_dir.txt','Run_Pkg_Installation_test.py']
    for item in file_list:
        zf.write(item)

with zipfile.ZipFile('log_all.zip','r') as zf:
    unzip_folder = 'unzipped_content'
    zf.extractall(unzip_folder)
    zipped_files = os.listdir(unzip_folder)
    print(zipped_files)

