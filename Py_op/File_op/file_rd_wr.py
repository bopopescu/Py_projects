from shutil import copyfile, copy2 # copytree
import os
import shutil

#___________________________________________________________________________
with open("outfile.txt", "w") as output:
    my_list =[]
    in_file = r"logging_test.txt"

    with open(in_file, "r") as input:
        for line in input:
            my_list.append(line)
            if len(my_list) == 5:
                output.writelines(my_list)
                #writelines(list): write a list of strings to file
                del my_list[:] #my_list.clear()
        output.writelines(my_list)
        # print(my_list)
        # ['2018-02-10 18:33:52,527 - DEBUG- End\n', '2018-02-10 18:33:52,527 - INFO- The log\n',
        #  '2018-02-10 18:33:52,527 - WARNING- An\n', '2018-02-10 18:33:52,527 - ERROR- An err.\n']

#___________________________________________________________________________

out_file = "outfile_1.txt"
with open(out_file,"w") as output:
    in_file = r"logging_test.txt"

    with open(in_file,"r") as input:
        for line in input:
            output.write(line)
            # write(string): write a string as a line to a file.
        # write(arg) expects a string as argument and writes it to the file.
        # If you provide a list of strings, it will raise an exception (btw, show errors to us!).


#_______________________________________________________________________________
#_______________________________________________________________________________

#with open(source, 'r') as src, open(dest, 'w') as dst: dst.write(src.read())
#f.read() reads the file as an individual string, and so allows relatively easy
# file-wide manipulations, such as a file-wide regex search or substitution.
#f.readline() reads a single line of the file

infile = r"logging_test.txt"
newfile = r"outfile_2.txt"
with open(infile, "r") as input:
    with open(newfile, "w") as output:
        for i in input:
            output.write(i)

newfile = r"newfile.txt"
with open(infile, "r") as input:
    with open(newfile, "w") as output:
        a = input.readlines()
        # readlines(): read the whole file into a list of strings, each line corresponds to one line.
        # read(): read the  the whole file into a single string.

        # writelines(list_of_string): write a list of strings to a file
        # write(string): write a single string to a file.
        print(a)
        output.writelines(a)

#___________________________________________________________________________
#___________________________________________________________________________

infile = r"logging_test.txt"
append_file = r"app_file.txt"

with open(append_file,'a') as output:
    with open(infile, 'r') as input:
        for line in input:
            output.write(line)
        output.writelines(['\n','\n','End of the first write\n'])

with open(append_file,'a') as output:
    with open(infile, 'r') as input:
        for line in input:
            output.write(line)
#
# 2018-02-10 18:33:52,527 - DEBUG- End
# 2018-02-10 18:33:52,527 - INFO- The log
# 2018-02-10 18:33:52,527 - WARNING- An
# 2018-02-10 18:33:52,527 - ERROR- An err.
#
#
# End of the first write
# 2018-02-10 18:33:52,527 - DEBUG- End
# 2018-02-10 18:33:52,527 - INFO- The log
# 2018-02-10 18:33:52,527 - WARNING- An
# 2018-02-10 18:33:52,527 - ERROR- An err.
#___________________________________________________________________________
