import time
import sys
import os

# os.system("pause")
###################################################################################################
####
# zip, map, and filter all return an iterator
# zip takes tuple of iterables and return an iterable of tuples
dic1 = {'wifi': 1, 'bt': 2}
dic2 = {'abgn': 3, 'ax': 4}

merg1 = zip(dic1, dic2, dic2, dic2)
# [('wifi', 'abgn', 'abgn', 'abgn'), ('bt', 'ax', 'ax', 'ax')]
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
list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three', 'six']

iter_zip = zip(list1, list2)
print(f"type(iter_zip) is {type(iter_zip)}")  # type(iter_zip) is <class 'zip'>
a, b = zip(*iter_zip)
print(f"type(a) is {type(a)}, and a is {a}\ntype(b) is {type(b)}")
# type(a) is <class 'tuple'>, and a is ('Alpha', 'Beta', 'Gamma', 'Sigma')
print(list(a))
# ['Alpha', 'Beta', 'Gamma', 'Sigma']

list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
# list is iterable, but not iterator
# iter(list) turn a list to an iterator
# print(next(list1))
list1 = iter(list1)
try:
    while True:
        item_a = next(list1)
        print(item_a, end=", ")
except:
    print("\ndone")
# Alpha, Beta, Gamma, Sigma,
# done
####
x = lambda a : a + 10
print(x(5))

t = lambda a, b : a+ b
print(t(100, 1))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

#@@
Input: ["23:59", "00:00"]

def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        tp = sorted(map(int, p.split(':')) for p in timePoints)
        tp += [[tp[0][0] + 24, tp[0][1]]]
        return min((tp[x+1][0] - tp[x][0]) * 60 + tp[x+1][1] - tp[x][1]
                   for x in range(len(tp) - 1))

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
