#os.rename(oldname, newname) # rename a file or folder
#os.remove() removes a file.

#os.rmdir() removes an empty directory.

#shutil.rmtree() deletes a directory and all its contents.

#pathlib.Path.unlink() removes the file or symbolic link.

#pathlib.Path.rmdir() removes the empty directory
#
#By design, rmtree fails on folder trees containing read-only files.
#If you want the folder to be deleted regardless of whether
#it contains read-only files, then use
#shutil.rmtree('/folder_name', ignore_errors=True)
import os
#os.makedirs("dir\dir1")
#os.mkdir("dir\dirs") # error: mkdir can't make nested directory
#os.path.abspath()
#os.path.split

filename = "b_file_op2.py"
file_path = os.path.abspath(filename) # give full path :  'C:\\Users\\jsun\\Documents\\PyProj\\file_op\\b_file_op2.py'
path_list = os.path.split(file_path)

print(type(path_list)) #<class 'tuple'>
print(path_list) #('C:\\Users\\jsun\\Documents\\PyProj\\file_op', 'b_file_op2.py')

file_path = path_list[0]
path_list = os.path.split(file_path)
print(path_list) # ('C:\\Users\\jsun\\Documents\\PyProj', 'file_op')


from glob import glob
import os
from datetime import datetime
schfile = os.path.join(os.getcwd(),"**","*.txt")
#a = glob(schfile, recursive=True)
#for i in a:
 #   print(i)

a = os.stat("file_test.py")
print(os.stat("file_test.py"))
print(type(os.stat("file_test.py")))

print("size is {} bytes".format(a.st_size))
print("atime is {}".format(datetime.fromtimestamp(a.st_atime).strftime("%Y_%m_%d_%H_%M_%S")))
print("mtime is {}".format(datetime.fromtimestamp(a.st_mtime).strftime("%Y_%m_%d_%H_%M_%S")))
print("ctime is {}".format(datetime.fromtimestamp(a.st_ctime).strftime("%Y_%m_%d_%H_%M_%S")))

