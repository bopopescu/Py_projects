from shutil import copyfile, copy2
import os
import shutil
#from pathlib import Path
#logoutput
#log1

cur_dir = os.chdir("logoutput")
#read() return a string for the whole content
#read(n) return content of n bytes, upto 5555 bytes
#readlines(n) n is bytes too


file_name = "log1.txt"
"""
with open(file_name, 'r') as infile:
    #text = infile.read()# return a string
    
    print(infile.tell()) # 0
    text = infile.read(99)
    print(infile.tell()) # 101
    #infile.seek(101)
    tarr = []
    tarr.append(text)
    print(tarr)

    text = infile.read(99)
    print(infile.tell())
    tarr.append(text)
    print(tarr)

with open(file_name, 'r') as infile:
    tarr = []
    text = infile.read(100)
    while text:
        tarr.append(text)
        print(infile.tell(), text)
        text = infile.read(100)

    print("*"*10)
    print(infile.tell())
    print(tarr)
"""


#"""
with open(file_name, 'r') as infile:
    text = infile.read().splitlines()# a list of strings stripped of "\n"
    #print(text)

#readline(n) is same as readlines() still read the whole thing
with open(file_name, "r") as f:
    lines = f.readlines(1) # same as f.read().splitlines()
    print(f.tell())
    #print(type(lines)) # list of strings
    for line in lines:
        pass
        #print(line)

def read_line_by_line():
    with open(file_name, "r") as f:
        line = f.readline()
        lines = []
        while line:
            #print(f.tell())
            lines.append(line)
            line = f.readline()
        print(lines)

read_line_by_line()

def iterate():
    with open(file_name, "r") as f:
        lines = []
        for line in f: # read line by line
            lines.append(line)
        print(lines)
iterate()

with open(file_name, "r") as ins:
    x = [ l.strip() for l in ins]
    print(x)

#"""