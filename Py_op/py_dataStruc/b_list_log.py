
#nums is a list
import copy
reverse() vs reversed()
sort() vs sorted()
nums.reverse()

max, min

#@@ 1. list passed as an argument
arr = [[100,200],2,3,4,5]

def change_list(arr):
    arr[0][0]= 20000
    arr[1] = 999
    # arr[4]  = 99 IndexError: list assignment index out of range

change_list(arr[0:2]) # arr[0:2] is shallow copy of arr[0:2]; it is a new list of size 2.
print(f"arr is {arr}") # arr is [[20000, 200], 2, 3, 4, 5]

change_list(arr)  #  arr is  arr, not  a shallow copy of arr
print(f"arr is {arr}") # arr is [[20000, 200], 999, 3, 4, 5]

a_tuple = ([1,2],3)
print(type(a_tuple), a_tuple)

# a_set = {[1,2],3}  TypeError: unhashable type: 'list'
# print(type(a_set), a_set)

#@@ 1.1  list passed to a function
s = [1,2,3]
def no_change_to_list(s):
    s[0] = 100
    return s

no_change = no_change_to_list(s[0:2])
print(f"no change is {no_change}")
print(f's is not changed {s}')
# no change is [100, 2]
# s is not changed [1, 2, 3]

#@@ 2.
str = "  this is  a good book  "
str_list_1 = str.split(" ") #   ['', '', 'this', 'is', '', 'a', 'good', 'book', '', '']
str_list_2 = str.split()     #  ['this', 'is', 'a', 'good', 'book']

#@@ 3.
p = [10,3,0,5,3]
sp = [2,10,1,1,3]
p_s = list(zip(p,sp))
print(p_s)
# [(10, 2), (3, 10), (0, 1), (5, 1), (3, 3)]

p_s1 = dict(p_s)  # {10: 2, 3: 3, 0: 1, 5: 1}

ps = sorted(p_s, key = lambda x: (x[0], x[1]))
# [(0, 1), (3, 3), (3, 10), (5, 1), (10, 2)]
print(ps)

pss = sorted(p_s, key = lambda x: (x[0], x[1]),reverse= True)
print(pss)
# [(10, 2), (5, 1), (3, 10), (3, 3), (0, 1)]

psss = sorted(p_s, key = lambda x: x[0])
print(psss)
# [(0, 1), (3, 10), (3, 3), (5, 1), (10, 2)]

pssss = sorted(p_s, key = lambda x: x[1])
print(pssss)
# [(0, 1), (5, 1), (10, 2), (3, 3), (3, 10)]

# sorted() doesn't change current list, but return a new sorted list
a = [5, 1, 4, 3]
sort_t = sorted(a)  # [1, 3, 4, 5]
print(a)  # [5, 1, 4, 3]#sorted
strs = ['aa', 'BB', 'zz', 'CC']
strs_sort = sorted(strs)  # ['BB', 'CC', 'aa', 'zz']
strs_rev = sorted(strs, reverse=True)  # ['zz', 'aa', 'CC', 'BB']

strs1 = ['ccc', 'aaaa', 'd', 'bb', 'AAAA']
# ['d', 'bb', 'ccc', 'aaaa', 'AAAA'], for same len, order is random
strs1_st = sorted(strs1, key=len)
sorted(strs, key=str.lower)  # ['aa', 'BB', 'CC', 'zz']
(sorted(strs, key=str.upper))

#@@ 4.
ss = ['b','B']
sss='bB'
# d = sorted(ss, key=str.lower)

print(f"ss[0:0] is !{ss[0:0]}!") # ss[0:0] is ![]!
print(f"ss[5:] is !{ss[5:]}!") # ss[5:] is ![]!
print(f"ss[-5:-3] is !{ss[-5:-3]}!") # ss[-5:-3] is ![]!
print(f"sss[0:0] is !{sss[0:0]}!") # ss[0:0] is !!
print(f"sss[3:] is !{sss[3:]}!") # sss[3:] is !!
# print(f"sss[3] is !{sss[3]}!") # IndexError: string index out of range

#@@ 5.

for __ in range(4):
    print(1)
    print()

#==, !=
# and , or,
if nums[left] <= target <= nums[mid]:
if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
nums[current - 1], nums[i] = nums[i], nums[current - 1]

#@@ 6.
a = [1,2]
v = 3
print(a + [v])#[1, 2, 3]
print(a) #[1, 2]

#@@ 7. empty array
rs = []
a = list()
a.append(100)

#@@ 8.
maxh = [0 for __ in range(5)]
print(maxh) #[0, 0, 0, 0, 0]
#4.
arr = [0]*5
print(arr) #[0, 0, 0, 0, 0]

#@@ 9.
#range(start, stop, step), is iterable, but not iterator
for i in range(4,1,-1):
    print(i," ", end="") #4  3  2  , exclude end = 1
print()

for i in range(5, -1, -1): #won't work range(5,-1)
    print(i," ", end="") #5 4  3  2  1  0 exclude end = -1
print()

#@@ 10.
from pprint import pprint
a = [ [0]*5 for __ in range(5)]
a[0][0] = 99
a[4][4] = 88
pprint(a)
#Create 2-D array
# [[99, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 88]]

from pprint import pprint
row = 4
col = 10
dp = [[1 for __ in range(col)] for __ in range(row)]
pprint(dp)
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

#@@ 11. generator
numbers = range(1_0) #<class 'range'>
squares = (n**2 for n in numbers) #<class 'generator'>, generator is an iterator
try:
    while True:
        print(next(squares))
except:
    print("done")

squares = [n**2 for n in numbers]#<class 'list'>
new_list = list(n*n for n in range(5))
#squares = n**2 for n in numbers  #error
print(type(squares))
print(type(numbers))

#@@ 12.
rs = []
rs = [[8]+ [4] for r in range(5)]
#[[8, 4], [8, 4], [8, 4], [8, 4], [8, 4]]

result = [[]]
#10
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum)  # 30

##
ss = sum(squares)
print(ss)
#######################

#@@ 13.
a = (n*n for n in range(5))
print(type(a)) #<class 'generator'>
b = []
b.extend(a)
print(b) #[0, 1, 4, 9, 16]

#@@ 14.
case = ["wifi"]
case1 = ['wifi']
print(case==case1) #True
print(case is case1) #False

case = ("wifi")
case1 = ('wifi')
print(case==case1) #True
print(case is case1) #True

case = (["wifi"])
case1 = (['wifi'])
print(case==case1) #True
print(case is case1) #False
#search an element in a list

spam = ('hello', 'goodbye')
eggs = ('hello', 'goodbye')
print(spam is eggs) #False

#@@ 15.
my_tuple = ("hello")
print(type(my_tuple)) #str

my_tuple = ("hello",)
print(type(my_tuple))#tuple
tuple = (1, 2, 'hi')  # (1, 2, 'hi')
len(tuple)  # 3
tuple[2]  # hi
# tuple[2] = 'bye'  # NO, tuples cannot be changed
tuple = (1, 2, 'bye')  # this works (1, 2, 'bye')

#@@ 16
def all_indices(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices

all_indices("testID", ["testID","testr","station","testID"])


#@@ 17
#Shallow copy
ls = [[1,2,3],"wifi","bt","tk"]
cp = ls.copy()

ls[0][0]=[1,23]
print("cp is ", cp)
print("ls is ",ls)
print(id(cp), ", ", id(ls))
# cp is  [[[1, 23], 2, 3], 'wifi', 'bt', 'tk']
# ls is  [[[1, 23], 2, 3], 'wifi', 'bt', 'tk']
# 2924848129544 ,  2924846536456
#
ls = [[1,2,3],"wifi","bt","tk"]
cp = ls.copy()
ls[0]=[100]
print("cp is ", cp)
print("ls is ",ls)
#cp is  [[1, 2, 3], 'wifi', 'bt', 'tk']
#ls is  [[100], 'wifi', 'bt', 'tk']
#
ls = [[1,2,3],"wifi","bt","tk"]
cp = ls.copy()
ls[1]= 100
print("cp is ", cp)
print("ls is ",ls)
print(id(cp), ", ", id(ls))
cp is  [[1, 2, 3], 'wifi', 'bt', 'tk']
ls is  [[1, 2, 3], 100, 'bt', 'tk']
2216888944136 ,  2216887379720

##

nums = [[1, 2], 1, 100]
new_nums = nums.copy()
new_new = copy.deepcopy(nums)

nums[0][0] = 1000
print("nums is {}".format(nums))
print("new_nums is {}".format(new_nums))
print("new_new is {}".format(new_new))
nums is [[1000, 2], 1, 100]
new_nums is [[1000, 2], 1, 100]
new_new is [[1, 2], 1, 100]

#@@ 18
a = ["foo","bar","baz",'bar','any','much']
indexes = [index for index in range(len(a)) if a[index] == 'bar']

rst = [i for i,j in enumerate(a) if j == 'bar']
print(rst)
#
test = ["wifi", "bt",'ac']
if "ac" in test:
    print("a")
else:
    print( None)

#@@ 19
tu = ("wifi", "agn", "ac", "ax", "bt")
print('{0} {2} {1} {2} {3} {2} {4} {2}'.format(*tu))  # wifi ac agn ac ax ac bt ac


#@@ 20
# list.extend(1)  #TypeError: 'int' object is not iterable
test = ["wifi", "bt",'ac',"11ax","ad"]
test[1:-1]       #['bt', 'ac', '11ax'], skip the first one and the last one
print(test[1:])      #['bt', 'ac', '11ax', 'ad'] skip the first one

print(test[1:4:2])   #['bt', '11ax']
test[1:3] = ["ac","BT"] # ['wifi', 'ac', 'BT', '11ax', 'ad']

test[:]                 # ['wifi', 'ac', 'BT', '11ax', 'ad']
test[::-1]              #reverse list, ['ad', '11ax', 'BT', 'ac', 'wifi']

test[-1]                #last element "ad"

# a[start:]    # items start through the rest of the array
# a[:end]      # items from the beginning through end-1
# a[:]         # a copy of the whole array

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

#
a = [0,1,2,3,4]
print(a[::-1])# [4, 3, 2, 1, 0]
print(a[:3:-1]) #[4]
print(a[:2:-1]) #[4,3]
print(a[1:2:-1]) #[]
print(a[:-3:-1]) #[4,3]
print(a[1::-1]) #[1,0]

#@@ 21 
print(range(10)) #range(0, 10)

print(list(range(2, 20, 3))) # Output: [2, 5, 8, 11, 14, 17]

t_str = "automation test"
for i, v in enumerate(t_str):
    print(i, v, end=", ")
#0 a, 1 u, 2 t, 3 o, 4 m, 5 a, 6 t, 7 i, 8 o, 9 n, 10  , 11 t, 12 e, 13 s, 14 t,

t_str = "auto test"
t_enum = list(enumerate(t_str))
print(type(t_enum)) #<class 'list'>
print(t_enum)
#[(0, 'a'), (1, 'u'), (2, 't'), (3, 'o'), (4, ' '), (5, 't'), (6, 'e'), (7, 's'), (8, 't')]

print(ord('a')-ord('A')) # 32
print(chr(32)) # 1

#@@ 22
left = list(filter(lambda x: x.end < start, intervals))
right = list(filter(lambda x: x.start > end, intervals))

#ADD
#list.append(elem) -- adds a single element to the end of the list.does not return the new list, just modifies the original.
#list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
#list.extend(list2)--list2 must be a list or iterable; adds the elements in list2 to the end of the list.
#Using + or += on a list is similar to using extend().

#search
#list.index(elem) -- searches the given element and returns its index.
#list.index(elem,start_pos)
#Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
#i = somelist.index(x) if x in somelist else None

#sort
#list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
#list.reverse() -- reverses the list in place (does not return it)

##
#list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError
##list.pop(index) -- removes and returns the element at the given index.
#list.pop() -- remove the last element, and return the element being removed

a = list((1,))
print(type(a), a) # [1]

b = ['wifi', 'bt']
b = [1] + b + [2]
print(b) #[1, 'wifi', 'bt', 2

#@@ 23
arr = []
if not arr:  # True
    print("arr is empty")
if arr == []: # True
    print("arr == []")
if len(arr) == 0: # True
    print("len(arr) == 0")
if arr == None: # False
    print("arr == None")

#@@ 24
matrix = [[]] # matrix is NOT empty
if not matrix: # False
    print("empty row")
else: # num of row in matrix len(matrix) is  1
    print("num of row in matrix len(matrix) is ", len(matrix))

if not matrix[0]: # True
    print("empty column")  # empty column
    # len(matrix[0]) : num of columns

arr2 = [[1]*3 for _ in range(5)]
print(" num of row: {}\n num of column: {}".format(len(arr2), len(arr2[0])))
# num of row    len(arr2:     5
# num of column len(arr2[0]): 3

#@@ 25
matrix = []
print(len(matrix)) # 0
matrix.append([])
print(len(matrix)) # 1
matrix.append([])

print(len(matrix), len(matrix[0])) # 2, 0
matrix[0].append(2)
matrix[1].append(3)

##
matrix = [[]]
print("len of matrix ", len(matrix)) # 1
matrix.append([])
print("len of matrix ", len(matrix))  #2
matrix.append([])
print("len of matrix ", len(matrix))  # 3

##
mm = [[] for _ in range(5)]

print(len(mm), len(mm[0]))  # 5 0

#@@ 26
#
arr = [(100,'wifi',5),(34,'opt',88), (34,'opt', 45),(99, 'ac', 'ka')]
print(arr)
arr.sort()
print(arr)
print(sorted(arr))
# [(100, 'wifi', 5), (34, 'opt', 88), (34, 'opt', 45), (99, 'ac', 'ka')]
# [(34, 'opt', 45), (34, 'opt', 88), (99, 'ac', 'ka'), (100, 'wifi', 5)]
# [(34, 'opt', 45), (34, 'opt', 88), (99, 'ac', 'ka'), (100, 'wifi', 5)]

t = [(100,100,100),(200,200,0),(100,100,0),(200,200,200),(0,255,0)]
t1 = sorted(t, key = lambda x: (x[0], x[1], x[2]))
print("t1 ", t1)
import operator
t.sort(key = operator.itemgetter(0, 1, 2))
print("t ", t)

# t1  [(0, 255, 0), (100, 100, 0), (100, 100, 100), (200, 200, 0), (200, 200, 200)]
# t  [(0, 255, 0), (100, 100, 0), (100, 100, 100), (200, 200, 0), (200, 200, 200)]
##
arr = [1,2,3,4,5,6,7,8]
print(arr[:-4]) #[1, 2, 3, 4]

#@@ 27
ltr_str = "abcd"
ltr_list = ltr_str.split("") # ValueError: empty separator

# convert string to a list or a tuple
In[11]: tuple("Test")
Out[11]: ('T', 'e', 's', 't')

In[12]: list("Station")
Out[12]: ['S', 't', 'a', 't', 'i', 'o', 'n']

In[13]: tuple(50)
---------------------------------------------------------------------------
TypeError                                 Traceback(most recent call last)
<ipython-input-13-a3e64f0fb23c > in < module >
--- -> 1 tuple(50)

TypeError: 'int' object is not iterable

In[14]: tuple(50,)
---------------------------------------------------------------------------
TypeError                                 Traceback(most recent call last)
<ipython-input-14-cd94c614be7d > in < module >
--- -> 1 tuple(50,)

TypeError: 'int' object is not iterable

In[15]: list(50)
---------------------------------------------------------------------------
TypeError                                 Traceback(most recent call last)
<ipython-input-15-8e20b6aa43ab > in < module >
--- -> 1 list(50)

TypeError: 'int' object is not iterable
