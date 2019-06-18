# string function
# partition, index, replace,
title = "Recipe 5: Rewriting, and the Immutable String"
colon_position = title.index(':')

title_a = "This is First : and Then Second : and Tail"
a = title_a.partition(':') # type of tuple
print(type(a))
#('This is First ', ':', ' and Then Second : and Tail')

title = title_a.replace(':', '-')
#title: This is First - and Then Second - and Tail

for letter in title:
    if letter == ' ':
        title_colon = title.replace(letter, "$")
# title_colon is  This$is$First$-$and$Then$Second$-$and$Tail

title_lower = title.lower()
# title_lower is  this is first - and then second - and tail

#.strip('-') takes away '-' in the beginning or end of a tring
test = "--po--st--"
test_strip = test.strip('-')
# test_strip is  po--st

a = [123, 'xy', 'zara', 'abc']
if a.count('xy') == 1:
    pos = a.index('xy')
    #pos is 1

aList = [123, 'xyz', 'zara', 'abc']
b_list = [456,789]
aList.append(2009)
# aList: [123, 'xyz', 'zara', 'abc', 2009]
c_list =[]
c_list.extend(b_list)
# cList: Updated c_list :  [456, 789]
aList.append(b_list)
# aList updated: Updated a_list :  [123, 'xyz', 'zara', 'abc', 2009, [456, 789]]

list1 = [123, 2,980,40]
list3 = list1 + [786] # like extend
#list3: [123, 2, 980, 40, 786]
#max: 980


tub1 = (1) # () doesn't make tub1 of tube type
#1
#tub1 <class 'int'>
tub2 = (2,) #tuple type
print("tub2 is type: {}".format(type(tub2)))

list_1  = [1]
print("list_1 is of type: {}".format(type(list_1)))
print (r"\n") #\n
print (R"\n") #\n

print (" this is a test \
this is a follow up")

str1 = "this is string example....wow!!!"
str2 = "exam"

print (str1.find(str2)) #15
print (str1.find(str2, 10)) #15
print (str1.find(str2, 40)) #-1

num = { "Cynthia":"223", "Raymond":"564", "David": "980"}
for key in num.keys():
    print(key, ": ", num[key], "")

num = range(1,11)
EN = [x for x in num if x%2==0]
#[2, 4, 6, 8, 10]

print("my name is {0} and my wh is {1}.".format("a",100))
#my name is a and my wh is 100.



def log(arr):
    a = arr
    a.append("HDR")
    print("a is {}".format(a))
    return a


if __name__ == "__main__":
    test_list = ["wifi", 'SU', 'OFDMA']
    b = log(test_list)
    print("b is {}".format(b))
    print("test_list is {}".format(test_list))

a is ['wifi', 'SU', 'OFDMA', 'HDR']
b is ['wifi', 'SU', 'OFDMA', 'HDR']
test_list is ['wifi', 'SU', 'OFDMA', 'HDR']

a =["SU","OFDMA"]
b = a
b.append("HDR")

print("a is {}".format(a))
print("b is {}".format(b))

a is ['SU', 'OFDMA', 'HDR']
b is ['SU', 'OFDMA', 'HDR']


def log(arr):
    a = arr
    # a.append("HDR")
    a = "HDR"
    print("a is {}".format(a))
    return a


if __name__ == "__main__":
    test_list = "WIFI"
    b = log(test_list)
    print("b is {}".format(b))
    print("test_list is {}".format(test_list))

a is HDR
b is HDR
test_list is WIFI


def log(arr):
    #a = arr
    #a.append("HDR")
    arr = "HDR"
    print("arr is {}".format(arr))
    return arr


if __name__ == "__main__":
    test_list = "WIFI"
    b = log(test_list)
    print("b is {}".format(b))
    print("test_list is {}".format(test_list))

arr is HDR
b is HDR
test_list is WIFI

def log(arr):
    arr = ["BT","LE"]
    print("arr is {}".format(arr))
    return arr


if __name__ == "__main__":
    test_list = ["wifi", 'SU', 'OFDMA']
    b = log(test_list)
    print("b is {}".format(b))
    print("test_list is {}".format(test_list))

    arr is ['BT', 'LE']
    b is ['BT', 'LE']
    test_list is ['wifi', 'SU', 'OFDMA']

##
from pprint import pprint
"""
bd = [[0]*8]*8
row = [0]*8
bd = [row]*8
"""
#bd = [[0]*8 for i in range(8)]
#print(bd)
bd = [ [0]*8 for i in range(8)]

pprint(bd)
bd[0][0]=1
pprint(bd)

###
import queue

test_q = queue.Queue()
for i in range(10):
    test_q.put(i*10)

print(test_q.qsize())
while not test_q.empty():
    print(test_q.get(), end=", ")
