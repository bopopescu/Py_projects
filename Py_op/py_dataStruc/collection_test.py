import time
import sys
import os

# os.system("pause")
###################################################################################################
####
# zip, map, and filter all return an iterator

dic1 = {'wifi': 1, 'bt': 2}
dic2 = {'abgn': 3, 'ax': 4}

merg = zip(dic1, dic2)
print(list(merg)) #[('wifi', 'abgn'), ('bt', 'ax')]

#
list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three', 'six']

# zip returns an iterator
test = zip(list1, list2)  # zip the values # test is an iterator
try:
    while True:
        item_a, item_b = next(test)
        print(item_a, item_b)
except:
    print("done")
# time.sleep(1000)
# ('Alpha', 'one'), ('Beta', 'two'), ('Gamma', 'three'), ('Sigma', 'six')
test = zip(list1, list2)
testList = list(test)

#
a, b = zip( *testList )
print('The first list was ', list(a))
print('The second list was ', list(b))

####
x = lambda a : a + 10
print(x(5))

t = lambda a, b : a+ b
print(t(100, 1))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

#map returns an iterator
def multiply2(x):
    return x * 2

a = map(multiply2, [1, 2, 3, 4])  # Output [2, 4, 6, 8]

print(type(a), a, sep=", ")
for i in a:
    print(i, sep=", ")
#
def to_upper_case(s):
    return str(s).upper()
def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line

# map returns an map object, which is an iterator
map_iterator = map(to_upper_case, 'abc')
print(type(map_iterator))
print_iterator(map_iterator)
#
def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line
list_numbers = [1, 2, 3, 4]

map_iterator = map(lambda x: x * 2, list_numbers)
print_iterator(map_iterator)
#
list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8)
map_iterator = map(lambda x, y: x * y, list_numbers, tuple_numbers)
print_iterator(map_iterator)
# filter returns an iterator
list_of_dict = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

map(lambda x: x['name'], list_of_dict)  # Output: ['python', 'java']

map(lambda x: x['points'] * 10, list_of_dict)  # Output: [100, 80]

map(lambda x: x['name'] == "python", list_of_dict)  # Output: [True, False]
a = [1, 2, 3, 4, 5, 6]
b=filter(lambda x : x % 2 == 0, a) # Output: [2, 4, 6]

list_of_dict = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
b = filter(lambda x : x['name'] == 'python', list_of_dict)  # Output: [{'name': 'python', 'points': 10}]

#
from collections import Counter
# Counter is a sub-class of dict, has all dict's interfaces
# elements() returns an iterator
# most_common() returns a list of tuple of key and value

collect_b = Counter({"cnt": "br", "cnt1": "ac"})
b_ele = collect_b.elements()
#
print("start b_ele")
try:
    while True:
        print(next(b_ele))
except:
    print()

b_most_common = collect_b.most_common(1)
print("b_most_common type is ", type(b_most_common))
print(b_most_common) #[('cnt', 'br')


a = Counter({'a': 2, 'b': 1, "c": 3, 'd': 3})
a_elements = a.elements()
print("Counter a type is ", a_elements)

try:
    while True:
        print(next(a_elements), end=", ")
        # time.sleep(1)
except:
    print() # a, a, b, c, c, c, d, d, d,

a_most_common = a.most_common(2) # most_common() return a list
print("a_most_common is ", a_most_common) # a_most_common is  [('c', 3), ('d', 3)]

a['a'] = 0
print("list of a.elements() is ", list(a.elements()))
print("a['a'] is ", a['a'])  # a['a'] is  0
# time.sleep(1000)

del a['a']
print("Counter is of".format(type(a)), list(a.elements()))

# time.sleep(1000)
#
from collections import Counter
str_dict = Counter("this contains multiple redundancy")

print("dict of str_dict is ", str_dict.most_common())
[('n', 4), ('t', 3), ('i', 3), (' ', 3), ('s', 2), ('c', 2), ('a', 2), ('u', 2), ('l', 2), ('e', 2), ('d', 2), ('h', 1), ('o', 1), ('m', 1), ('p', 1), ('r', 1), ('y', 1)]
#
print("dict of str_dict is ", str_dict.most_common(7))

# time.sleep(1000)

import collections

print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))

print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))

print(collections.Counter(a=2, b=3, c=1))

import collections

c = collections.Counter()
c.update("abcdaab")
print("*****", c, sep="    ")
c.update({"a": 10, "d": 5})
print(c)
c.update(["a", "e"])
print(c)

for letter in "abcde":
    print(letter, "--->", c[letter])
##
ad = lambda x, y : x+y
print(ad(10, 9))
arr1 = [ 2, 5, 6, 7]
arr2 = [ 10, 40, 60, 80]
cmap = map(lambda x: x % 2 == 0, arr1)
print(list(cmap))
cfilter = filter(lambda x: x %2==0, arr1)
print(list(cfilter))
list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 'd', 'e']
list_c = zip(list_a, list_b) #<zip object at 0x038144E0>
print(type(list_c))
#print(list(list_c))

for j in list_c:
    print("({0}, {1})".format(j[0], j[1]), end = ", ")
print()
#### deque
from collections import deque
# deque take a list as argument
list = ["wifi","bt","ax", "ac",'ac', 'ac']
deq = deque(list)
# add to the tail
deq.append("abgn")
# add to head
deq.appendleft("brcm")
print(type(deq), deq, sep=", ")
# remove from the end
print("deq.pop() ", deq.pop()) # deq.pop()  abgn
print(type(deq), deq, sep=", ")
# remove from the beginning
deq.popleft()
print(type(deq), deq, sep=", ") # <class 'collections.deque'>, deque(['wifi', 'bt', 'ax', 'ac', 'ac', 'ac'])
#
# deq.clear()
# count()
print(deq.count('ac')) # 3

#access deque
for i in range(4):
    print(deq[i], end=", ")
print() # wifi, bt, ax, ac,
# deq[0] beginning item, deq[-1] ending item
print("deq[-1] ", deq[-1]) # ac
time.sleep(1000)





