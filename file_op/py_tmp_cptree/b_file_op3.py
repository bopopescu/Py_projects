from shutil import copyfile, copy2 #copytree
import os
import shutil
from pathlib import Path


with open("output_file2.txt", "w") as output:
    my_list =[]
    in_file = "doc_dir.txt"

    with open(in_file, "r") as input:
        for line in input:
            my_list.append(line)
            if len(my_list) == 5:
                output.writelines(my_list)
                del my_list[:]
        output.writelines(my_list)

with open("output_file1.txt","w") as output:
    in_file = "doc_dir.txt"

    with open(in_file,"r") as input:
        for line in input:
            output.write(line)
        #write(arg) expects a string as argument and writes it to the file.
        # If you provide a list of strings, it will raise an exception (btw, show errors to us!).



#with open(source, 'r') as src, open(dest, 'w') as dst: dst.write(src.read())
#f.read() reads the file as an individual string, and so allows relatively easy
# file-wide manipulations, such as a file-wide regex search or substitution.
#f.readline() reads a single line of the file
