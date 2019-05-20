from __future__ import with_statement
########
test_items = ["wifi","ax","ac","bt"]
#print("{0},{2}".format(*test_items)) #"wifi", "ac"
#print(test_items)
ax_test = ["rsdb","rsdb_mimo","rxrx"]
#test_items[:2] = ax_test

test_items[:2] # ['wifi', 'ax']

# print(type(test_items[:2]))  #<class 'list'>

str_items = " ".join(test_items)
list_itme = str_items.split(" ")
print(list_itme)
str1 = "w,e,l,c,o,m,e"
print(str1.split(',',3))

test_case = "wifi, bt, ax, rsdb, ac"
keyword = "rsdb"
if keyword in test_case:
    print(keyword)

#print(list_items)
with open("new_log.txt","w+") as fw:
    #fw.write("\n".join(test_items))
    #fw.writelines("{} ".format(test_items))
    #fw.writelines("%s\n" %l for l in test_items)

    #fw.write(str_items + " key_point")
    #line = fw.readline()
    #print("this is read {}".format(line))
    fw.write(str_items + "uo"+"\n")
    fw.seek
    print(fw.tell())
    line = fw.read()
    print("this is read {}".format(line))
    print(fw.tell())
#with open("new_log.txt","r") as fr:
#    print(fr.read())

import json
my_data=["Hafsa Jabeen", "Reading and writing files in python", 78546]
json.dumps(my_data)

with open("jsonfile.json","w") as f:
    json.dump(my_data, f)
f.close()

file = open("new_log.txt", "rb")
#print(file.line_buffering)
#file_contents=file.buffer
for line in file:
    print(line)

print(5/4)
print(5//4)

import os
file_name, file_ext = os.path.splitext("script.txt")
print(file_name)
print(file_ext)

import glob
for csv_file in glob.glob("*wifi.csv"):
    print(csv_file)

import math
lt = [4, 8 ,9, 11, 15,16,19]
for i in lt:
    sq_n = math.sqrt(i)
    sqrt_n = int(math.floor(math.sqrt(i)))
    print(i, sq_n, sqrt_n)
########
 