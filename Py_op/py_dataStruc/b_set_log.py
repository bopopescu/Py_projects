# empty tuple
wifi = ()
wifi_ac = tuple()

# a tuple contains one element
test1 = ((),)
test2 = (2,)

testt = (["wifi"]) # type of list, not tuple
## set is unique and ordered
t_set = {1,2,3} #{1, 2, 3}
#print(t_set)

t_list = [1,2,3,2]
v_set = set(t_list) #{1, 2, 3}

a = {} # empty dict
b = set() # empty set

old_set = {1,2,3}
old_set.add(10)
old_set.update([7,8,9])

print(old_set) # {1, 2, 3, 7, 8, 9, 10}
old_set.update([11,12],{20,21}) #{1, 2, 3, 7, 8, 9, 10, 11, 12, 20, 21}
print(old_set)

# Get the ASCII number of a character
char = 'a'
number = ord(char)

# Get the character given by an ASCII number
char = chr(number)

"-"
x = 10
old_set.discard(x)
print("after removing 10, old_set is {}".format(old_set))
# discard: removes element  from the set. The .discard(x) operation returns None.

x = 9
old_set.remove(x)
print("after removing 9, old_set is {}".format(old_set))
# remove: removes element  from the set. If element  does not exist, it raises a KeyError

old_set.pop()
print("after popping, old_set is {}".format(old_set))
#This operation removes and return an arbitrary element from the set.
#If there are no elements to remove, it raises a KeyError.