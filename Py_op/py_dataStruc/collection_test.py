
#____________________________________________________________________________________
from collections import Counter
b = Counter("")
print(len(b)) # 0


a = Counter({'d': 2, 'b': 1, "c": 3, 'a': 3})

# ('d', 2), ('b', 1), ('c', 3), ('a', 3),
# for item in a.items():
#     print(item, end=", ")
# print()

a_elements = a.elements()
a_elements_1 = a.elements()
a_elements_str = a.elements()

# print(f"type(a_elements) is {type(a_elements)}")
# type(a_elements) is <class 'itertools.chain'>
# print(a_elements)
# <itertools.chain object at 0x02F04AD0>

# while True:
#     try:
#         print(next(a_elements), end=", ")
#     except:
#         print("end")
#         break
# d, d, b, c, c, c, a, a, a, end

# what to do with iterator
toList = list(a_elements)
# print(f"toList is {toList}")
# toList is ['d', 'd', 'b', 'c', 'c', 'c', 'a', 'a', 'a']
toSet = set(a_elements_1)
# print(f"toSet is {toSet}")
# toSet is {'b', 'a', 'c', 'd'}
toString = "".join(a_elements_str)
# print(f"type(toString) is {type(toString)}")
# type(toString) is <class 'str'>
# print(f"toString is {toString}")
# toString is ddbcccaaa


#@@ .most_common(), returns a list of ordered tuples
# .most_common(num)

rst = a.most_common()
# print(f"type(rst) is {type(rst)}")
# type(rst) is <class 'list'>
# print(f"rst is {rst}")
# rst is [('c', 3), ('a', 3), ('d', 2), ('b', 1)]

b = Counter({'a':3, 'd': 7, 'e': 3, 'd':5,  'b': 1, "c": 3, 'f': 3})
# rst = b.most_common()
# print(rst)
# [('d', 5), ('a', 3), ('e', 3), ('c', 3), ('f', 3), ('b', 1)]

# rst = b.most_common(1)
# print(rst)
# [('d', 5)]

# rst = b.most_common(3)
# print(rst)
# [('d', 5), ('a', 3), ('e', 3)]

c = Counter({'a':3, 'd': 7, 'e': 3, 'd':5,  'b': 1, "c": 3, 'f': 3})
c['a']=0
# print(c['a']) # 0
rst = c.most_common() # [('d', 5), ('e', 3), ('c', 3), ('f', 3), ('b', 1), ('a', 0)]
# print(rst)

d = Counter({'a':3, 'd': 7, 'e': 3, 'd':5,  'b': 1, "c": 3, 'f': 3})
d['a']=0
# print(d['a']) # 0
rst = d.most_common() # [('d', 5), ('e', 3), ('c', 3), ('f', 3), ('b', 1), ('a', 0)]
# print(rst)
d.pop('a')
rst = d.most_common() #  [('d', 5), ('e', 3), ('c', 3), ('f', 3), ('b', 1)]
# print(rst)

# Counter intialized with strings
from collections import Counter
str_dict = Counter("mumltlmee reum")
rst_lst = str_dict.most_common()
# [('m', 4), ('e', 3), ('u', 2), ('l', 2), ('t', 1), (' ', 1), ('r', 1)]
# print(rst_lst)

str_dict['m']  = 2
rst_lst = str_dict.most_common()
# print(rst_lst)
# [('e', 3), ('m', 2), ('u', 2), ('l', 2), ('t', 1), (' ', 1), ('r', 1)]
str_dict['m']  = 3
rst_lst = str_dict.most_common()
# print(rst_lst)
# [('m', 3), ('e', 3), ('u', 2), ('l', 2), ('t', 1), (' ', 1), ('r', 1)]

# Counter intialized with list
chr_lst = ['e','a','b','g','e','b','e','g','b']
chr_cnter =  Counter(chr_lst)
rst_lst = chr_cnter.most_common()
print(rst_lst)


















#__________________________________________________________________________________________
from collections import Counter
# Counter is a sub-class of dict, has all dict's interfaces, val is freq of key
# Take a list as input
# elements() returns an iterator
# most_common() returns a list of tuple of key and value

#@@ 1.0

# Counter intialized with strings
from collections import Counter
str_dict = Counter("this contains multiple redundancy")

print("dict of str_dict is ", str_dict.most_common())
[('n', 4), ('t', 3), ('i', 3), (' ', 3), ('s', 2), ('c', 2), ('a', 2), ('u', 2), ('l', 2), ('e', 2), ('d', 2), ('h', 1), ('o', 1), ('m', 1), ('p', 1), ('r', 1), ('y', 1)]
#
print("dict of str_dict is ", str_dict.most_common(7))
# [('n', 4), ('t', 3), ('i', 3), (' ', 3), ('s', 2), ('c', 2), ('a', 2)]

print("elements of str_dict is {}".format(list(str_dict.elements())))
# ['t', 't', 't', 'h', 'i', 'i', 'i', 's', 's', ' ', ' ', ' ', 'c', 'c', 'o', 'n', 'n', 'n', 'n', 'a', 'a', 'm', 'u', 'u',
#  'l', 'l', 'p', 'e', 'e', 'r', 'd', 'd', 'y']
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
# print(f"type(deq) is {type(deq)},  deq is {deq}")
# type(deq) is <class 'collections.deque'>,
# deq is deque(['brcm', 'wifi', 'bt', 'ax', 'ac', 'ac', 'ac', 'abgn'])

# remove from the end
print("deq.pop() ", deq.pop()) # deq.pop()  abgn
print(deq) #deque(['brcm', 'wifi', 'bt', 'ax', 'ac', 'ac', 'ac'])
# remove from the beginning
deq.popleft()
print(deq) # deque(['wifi', 'bt', 'ax', 'ac', 'ac', 'ac'])
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

# time.sleep(1000)

d = deque('12345')
# print(type(d[0]), d[0], d[1], sep=", ") # <class 'str'>, 1, 2

# d = deque(maxlen=30)
# d = deque([1,2,3,4,5])
# d.extendleft([0])   deque([0, '1', '2', '3', '4', '5'])
# print(d)
d.extend([6,7,8])
# print(d) # deque(['1', '2', '3', '4', '5', 6, 7, 8])

# class collections.deque([iterable[, maxlen]])
#
# Returns a new deque object initialized left-to-right (using append())
# with data from iterable. If iterable is not specified, the new deque is empty.
#
# In your example , buff = collections.deque([], 100),
#
# creates a new empty deque object buff, specified by the first argument, with maxlen 100.
# It means the deque object is bounded to a maximum length of 100.



