from shutil import copyfile, copy2
import os
import shutil
from pathlib import Path
#logoutput
#log1

cur_dir = os.chdir("logoutput")
#read() return a string for the whole content
#read(n) return content of n bytes, upto 5555 bytes
#readlines(n) n is bytes too


file_name = "log1.txt"
with open(file_name, 'r') as infile:
    #text = infile.read()# return a string
    print(infile.tell())
    text = infile.read(99)
    print(infile.tell())
    infile.seek(101)
    tarr = []
    tarr.append(text)
    #print(tarr)

with open(file_name,'r') as infile:
    text = infile.read().splitlines()# a list of strings stripped of "\n"
    #print(text)

with open(file_name, "r") as f:
    lines = f.readlines(40) # same as f.read().splitlines()
    #print(type(lines)) # list of strings
    print(lines)

def read_line_by_line():
    with open("file_name","r") as f:
        line = f.readline()
        lines = []
        while line:
            lines.append(line)
            line = f.readline()

def iterate():
    with open("file_name","r") as f:
        lines = []
        for line in f:
            lines.append(line)

with open("file_name","r") as ins:
    x = [ l.strip() for l in ins]