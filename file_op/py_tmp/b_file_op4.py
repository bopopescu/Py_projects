from shutil import copyfile, copy2 #copytree
import os
import shutil
from pathlib import Path

file_name = "output_file1.txt"
dst_file  = "cpy_output.txt"
try:
    os.remove(dst_file)
except:
    None
copy2(file_name, os.getcwd()+"\\"+ dst_file)

if os.path.isfile(dst_file):
    #os.remove(dst_file) # remove a file
    print("{} is deleted.".format(dst_file))



#with open(source, 'r') as src, open(dest, 'w') as dst: dst.write(src.read())
#f.read() reads the file as an individual string, and so allows relatively easy
# file-wide manipulations, such as a file-wide regex search or substitution.
#f.readline() reads a single line of the file
