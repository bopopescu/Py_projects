# dictionary not sorted by default

cnt_dict = {'a':4, 'b':8, 'c':10, 'd':4, 'e':10, 'f':5, 'h':5, 'g':5}
# print(len(cnt_dict)) # 8
chr_key = cnt_dict.keys()
# print(f"type(chr_key) is {chr_key}")
# print(list(chr_key)) ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'g']
# type(chr_key) is dict_keys(['a', 'b', 'c', 'd', 'e', 'f', 'h', 'g'])
num_values = cnt_dict.values()
# print(list(num_values)) [4, 8, 10, 4, 10, 5, 5, 5]
# print(f"type(num_values) is {type(num_values)}")
# type(num_values) is <class 'dict_values'>
item_tuple = cnt_dict.items()
# print(list(item_tuple)) [('a', 4), ('b', 8), ('c', 10), ('d', 4), ('e', 10), ('f', 5), ('h', 5), ('g', 5)]
# print(f"type(item_tuple) is {type(item_tuple)}")
# type(item_tuple) is <class 'dict_items'>


my_dic = dict([("ID", 1),("Test", "wifi")])# a list of tuples
#print(my_dic.get("Test")) # "wifi" , "return None if key is wrong"

#Some tuples can be used as dictionary keys (specifically, tuples that contain immutable values
#like strings, numbers, and other tuples). Lists can never be used as dictionary keys,
#because lists are not immutable

#Tuples can be used as values in sets whereas lists can not

wi = {"mimo", "rsdb",("a","b"),["c","d"]} #TypeError: unhashable type: 'list'

squares = {1:1, 2:4, 3:9, 4:16, 5:25}
#print(squares.pop(4)) #16
#
pre_test = {'wifi':1, "BT":2}
print(pre_test["wifi"]) #1

test = { "wifi": 2, "BT": 3, "AC":3}
a = test.items() #<class 'dict_items'>
#print(a) #dict_items([('wifi', 2), ('BT', 3), ('AC', 3)])
 
#Iterate over keys

for key, value in my_dic.items():

#Iterate over (key, value) tuples
for key, value in my_dictionary.items(): #key, value is just variables
for a, b in my_dictionary.items() # same results, a is key, b is its corresponding value

#Iterate over values
for value in my_dic.values():

#Iterate over keys
for key in my_dic:

#Check for existence
haystack = {}
# ...
if 'needle' in haystack:

b = d.items()
print("type b is {}".format(b))  # dict_items
# ([('MPS', 0), ('MPS_AC', 1), ('11AX', 2)])

# c = b[0] #TypeError: 'dict_items' object does not support indexing
# print("type c is {}".format(c))

#
#test = { "wifi": 2, "BT": 3, "AC":4}
test = dict([('wifi', 2),("bt",3),('AC',4)])
for value in test.values():
    print(value)
for key in test:
    print(key, test[key])
print("**********")
for a, b in test.items():
    print(b, a)
2
3
4
wifi 2
bt 3
AC 4
**********
2 wifi
3 bt
4 AC
#######################################################################
len(test)
#Add
test["MIMO"] = 10
#remove
test.pop("MIMO")
#rmv last item
test.popitem()
#
test.update({"MU-MIMO": 6})

#
test = dict([('wifi', 2),("bt",3),('AC',4)])
test_1 = [("mu",5),("su",6),("su", 7)]
test.update(test_1)
#
sorted(iterable_sequence)
sorted(iterable_sequence, reverse=True)
del test["MIMO"]
test.clear() # empty dic
#
for l,k in enumerate(test_id):
    print(l,k)
print(l)
print(type(test_id.values()))
print(test_id.get("wifik","NOT found"))
print(test_id.get("wifik"))

test_list = {1:["wifi","ax"]}
for key, value in test_list.items():
    print(key, value)

print(test_id)
print(list(test_id.items()))

rsdb = {'mu+mu':'txtx'}
rsdb.update({'mu+SU':'rxrx'})

rdb = [('mumu','txtx'),('sumu','rxtx')]
print(rsdb.get('mumu',0))

mumu = dict(('mumu','TXTX')) #wrong
mumu.update(("MUMU","RXRX")) #wrong

test1 = dict([(5,50),(6,60),(7,70),(8,80)])
test.update(test1)
for k, v in test.items():
    print(k, v)
#
dic1 = {"wifi": 1, "bt": 2, "rsdb": 3}
dic2 = dict([("wifi", 1), ("bt", 2), ("rsdb", 3)])

###
new_add = [("wifiz", 1), ("bzt", 2), ("rzsdb", 3)]
dic2.update(new_add)
for key in dic2.keys():
    print(key)

##Add
a = {"wifi": 0, "AX":1, "BT": 2}
b = dict([("wifi", 0), ("AX", 1), ("BT", 2)])

#sub
#a.pop(key)

#search (N)
# walk through
#a.items(), a.keys(), a.values()

ck = dict([(1,"wifi"), (2,"UWB"),(3, "OFDMA")])
dk = [(4,"wifi"),(5, "bt"), (6, "rsdb")]
ddk = dict(dk)

ck.update({10: "ax"})
ee = ck.items()
ee = list(ee)
for i in ee:
    print(i, end=", ")
# (1, 'wifi'), (2, 'UWB'), (3, 'OFDMA'), (10, 'ax'),