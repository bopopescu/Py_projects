from shutil import copyfile, copy2 # copytree
import os
import shutil
"""
with open("output_file2.txt", "w") as output:
    my_list =[]
    in_file = r"logoutput\log1.txt"

    with open(in_file, "r") as input:
        for line in input:
            my_list.append(line)
            if len(my_list) == 5:
                output.writelines(my_list)
                del my_list[:] #my_list.clear()
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
import os
src_dir = os.path.join(os.getcwd(), "logoutput")
os.chdir(src_dir)
infile = "log1.txt"
newfile = 'log2.txt'
newfile1 = "log3.txt"
with open(infile,"r") as input:
    with open(newfile, "w") as output:
        for i in input:
            output.write(i)

with open(infile, "r") as input:
    with open(newfile1, "w") as output:
        a = input.readlines()
        output.writelines(a)
"""

with open("write_log.txt", "w") as fout:
    text = []
    line = "wifi test passed."
    for _ in range(5):
        text.append(line)
    fout.writelines(text)

with open("write_log1.txt", "w") as fout:
    line = "wifi test passed."
    for _ in range(5):
        fout.write(line)