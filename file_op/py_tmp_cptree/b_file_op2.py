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
    print(my_list)
#['cla1.py\n', 'doc_dir.txt\n', 'ex_2.py\n', 'fun1.py\n', 'fun2.py\n', 'IQfact+_BRCM_4364_MPS_3.4.1.17.zip\n', 'QA_Auto.py\n', 'Run_Pkg_Installation.py\n', 'Run_Pkg_Installation_test.py\n', 'Run_QA.py\n', 'summ.py\n', 'test.py\n', 'test1.py\n', 'Verify.py\n']
"""
* read(size) >> size is an optional numeric argument and this func returns a quantity of 
*data equal to size. If size if omitted, then it reads the entire file and returns a long string with "\n"
appended for each element
read().splitlines(), returns a list of elements with "\n" removed

* readline() >> reads a single line from file with newline at the end

* readlines() >> returns a list containing all the lines in the file, with newline for each line

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
import os.path
import glob


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

