#258
def addDigits( num):
    while num >= 10:
        sum = 0
        while num > 0:
            sum += num %10
            num //= 10
        num = sum
    return num
def addDigits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    if sum < 10:
        return sum
    else:
        return addDigits(sum)
def addDigits(num):
    num_s = str(num)
    if len(num_s) == 1:
        return num
    else:
        sum = 0
        for i in num_s:
            sum += int(i)
        return addDigits(sum)
#443
def compress(chars):
    len_s = len(chars)
    total, cnt = 0, 0
    for i in range(len(chars)):
        if i < len_s - 1:
            if chars[i] == chars[i+1]:
                cnt += 1
            else:
                if cnt == 0:
                    total += 1
                else:
                    total += 1 + len(str(cnt + 1))
                cnt = 0
        else:
            if chars[i] != chars[i-1]:
                total += 1
            else:
                total += 1 + len(str(cnt + 1))
    return total
def compress(chars):
    prev_ch, loc_update, cnt = chars[0], 0, 1
    for i in range(1, len(chars)):
        if chars[i] == prev_ch:
            cnt += 1
        else:
            str_update = prev_ch + str(cnt) if cnt > 1 else ""
            if cnt == 1:
                chars[loc_update] = prev_ch
                loc_update += 1
            else:
                for item in str_update:
                    chars[loc_update] = item
                    loc_update += 1
            prev_ch = chars[i]
            cnt = 1
    str_update = prev_ch + str(cnt) if cnt > 1 else ""
    for item in str_update:
        chars[loc_update] = item
        loc_update += 1

    chars = chars[0:loc_update]
    print(chars)
    print(loc_update)
    return loc_update
def compress(chars):
    prev_ch, loc_update, cnt = chars[0], 0, 1
    for i in range(1, len(chars)):
        if chars[i] == prev_ch:
            cnt += 1
        else:
            str_update = prev_ch + (str(cnt) if cnt > 1 else "")
            for item in str_update:
                chars[loc_update] = item
                loc_update += 1
            prev_ch = chars[i]
            cnt = 1
    str_update = prev_ch + str(cnt) if cnt > 1 else ""
    for item in str_update:
        chars[loc_update] = item
        loc_update += 1

    chars = chars[0:loc_update]
    print(chars)
    print(loc_update)
    return loc_update
#14
#203

def rmtest(head, val):
    if not head:
        return head
    while head and head.val == val:
        head = head.next
    new_head = head
    while head and head.next:
        if head.next.val == val:
            tmp = head.next
            while tmp and tmp.val == val:
                tmp = tmp.next
            head.next = tmp
            head = tmp
    return new_head
def rmtest(head, val):
    if not head:
        return head
    if head.val == val:
        return rmtest(head.next, val)
    head.next = rmtest(head.next, val)
    return head
def rmtest(head, val):
    if not head:
        return head
    cur = head
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head.next if head.val == val else head
def rmtest(head, val):
    new_head = ListNode(0)
    # new_head = head
    pre = new_head

    while head:
        if head.val != val:
            pre.next = head
            pre = head
            head = head.next
        while head and head.val == val:
            head = head.next
        pre.next = head
        pre = head
        head = head.next if not head else None
    return new_head.next
def rmtest(head, val):
    if not head:
        return head
    head.next = rmtest(head.next, val)
    if head.val == val:
        return head.next
    return head
#543
#TreeNode
def diameterof Bt(root):
    rst=[0]
    max_diam(root, rst)
    return rst[0]

def max_diam(root, rst):
    if not root:
        return 0
    left_node = max_diam(root.left, max_val)
    right_node =max_diam(root.right, max_val)
    rst[0] = max(rst[0], left_node + right_node)
    max_val = max(left_node, right_node) + 1
    return max_val

#125
def isPal(str):
    i, j = 0, len(str)-1
    str = str.lower()
    while i < j:
        if str[i].isalnum() and str[j].isalnum():
            if str[i] == str[j]:
                i += 1
                j -= 1
            else:
                return False
        elif str[i].isalnum():
            j -= 1
        elif str[j].isalnum():
            i += 1
        else:
            j -= 1
            i += 1
    return True
#680
def helper(str, k):
    i, j = 0, len(str)-1
    while i < j:
        if i == k:
            i += 1
        if j == k:
            j -= 1
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True


def isPal(str):
    for i in range(len(str)+1):
        if helper(str, i):
            return True
    return False

x = lambda a : a + 10
print(x(5))

t = lambda a, b : a+ b
print(t(100,1))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#
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
#
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

map(lambda x: x['name'], dict_a)  # Output: ['python', 'java']

map(lambda x: x['points'] * 10, dict_a)  # Output: [100, 80]

map(lambda x: x['name'] == "python", dict_a)  # Output: [True, False]
a = [1, 2, 3, 4, 5, 6]
b=filter(lambda x : x % 2 == 0, a) # Output: [2, 4, 6]

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
b=filter(lambda x : x['name'] == 'python', dict_a) # Output: [{'name': 'python', 'points': 10}]

#
from collections import Counter
a = Counter({'a':2, 'b':1,"c":3})
print(a.elements())
a['a'] =0
print(list(a.elements()))
del a['a']
print(a.most_common())

#____

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
#
#905
def sortA( A):
    arr_len = len(A)
    rst = list(range(arr_len))
    i, j = 0, arr_len - 1
    for item in A:
        if item % 2 == 0:
            rst[i] = item
            i += 1
        else:
            rst[j] = item
            j -= 1
    return rst
#922
def test_sort(A):
    even = 0
    for odd in range(1, len(A), 2):
        if A[odd] & 1:
            continue
        else:
            while not A[even] & 1:
                even += 2
        A[odd], A[even] = A[even], A[odd]
    return A
#202
def ishtest(n):
    rst = set()
    while True:
        str_n = str(n)
        sum = 0
        for i in str_n:
            sum += (int(i))**2
            print ((int(i))**2)
        if sum == 1:
            return True
        elif sum in rst:
            break
        else:
            rst.add(sum)
            n = sum
    return False
#415
def add_str(num1,num2):
    return str(int(num1) + int(num2))
def add_str(num1,num2):
    i, j = len(num1)-1, len(num2)-1
    carry = 0
    rst = ""
    sum = 0
    while i >=0 or j >=0:
        sum += carry
        sum += (int(num1[i]) if i >= 0 else 0) + (int(num2[j]) if j >= 0 else 0)
        #sum += int(num2[j]) if j >= 0 else 0
        carry = sum // 10
        sum %=  10
        rst = str(sum) + rst
        sum = 0
        i -= 1
        j -= 1
    rst = str(carry) + rst if carry > 0 else rst
    print(rst)
    return rst

#438
def fdana(s,p):
    dict_p, dict_s = {}, {}
    for item in p:
        if item in dict_p:
            dict_p[item] += 1
        else:
            dict_p[item] = 1

    len_s, len_p = len(s), len(p)
    rst = []
    i = 0
    while i < len_s:
        if s[i] not in dict_p:
            i += 1
            if not dict_s:
                dict_s.clear()
            continue
        else:
            if s[i] not in dict_s:
                dict_s[s[i]] = 1
            else:
                dict_s[s[i]] += 1

            if len(dict_s) == len(dict_p):
                if dict_s == dict_p:
                    start_index = i - len_p + 1
                    rst.append(start_index)
                    i = start_index + 1
                    if dict_s[s[start_index]] > 1:
                        dict_s[s[start_index]] -= 1
                    else:
                        dict_s.pop(s[start_index])
                else:
                    if dict_s[s[i - len_p + 1]] > 1:
                        dict_s[s[i - len_p + 1]] -= 1
                    else:
                        dict_s.pop(s[i - len_p + 1])

                    i += 1
            else:
                i += 1

    print(rst)
    return rst
def fdana1(s,p):
    len_s, len_p = len(s), len(p)
    dict_s, dict_p = {}, {}
    rst = []
    for item in p:
        if item not in dict_p:
            dict_p[item] = 1
        else:
            dict_p[item] += 1
    for i in range(len(p)-1):
        if s[i] in dict_s:
            dict_s[s[i]] += 1
        else:
            dict_s[s[i]] = 1

    for i in range( len_p - 1, len_s):
        if s[i] in dict_s:
            dict_s[s[i]] += 1
        else:
            dict_s[s[i]] = 1
        if dict_s == dict_p:
            rst.append( i - len_p + 1)
        if dict_s[s[i - len_p + 1]] > 1:
            dict_s[s[i - len_p + 1]] -= 1
        else:
            dict_s.pop(s[i - len_p + 1])
    print(rst)
def fdana(s,p):
    dict_s = Counter(s[:len(p)-1])
    dict_p = Counter(p)

    rst = []
    for i in range(len(p)-1, len(s)):
        dict_s[s[i]] += 1
        if dict_p == dict_s:
            rst.append(i - len(p) + 1)
        if dict_s[s[i - len(p) + 1]] > 1:
            dict_s[s[i - len(p) + 1]]  -= 1
        else:
            del dict_s[s[i - len(p) + 1]]
    return rst

#770
J = "aA"
S = "aAAbbbb"
J1 = "z"
S1 = "ZZ"
def numtone(J, S):
    j_set  = set()
    for j in J:
        if j not in j_set:
            j_set.add(j)
    cnt = 0
    for s in S:
        if s in j_set:
            cnt += 1
    return cnt
#770
J = "aA"
S = "aAAbbbb"
J1 = "z"
S1 = "ZZ"
def numtone(J, S):
    print(type(s in J for s in S))
    print(type(s for s in S))
    return sum([s in J for s in S])
print(numtone(J,S))

print(time.time())
#709
def tolower(str):
    diff = ord('a') - ord("A")
    rst = ""
    for s in str:
        if  "A"<=s<="Z":
            s = chr(ord(s) + diff)
        rst = rst + s
    print(rst)
#
s = "QA test"
ss = (a if a > "A" else "QQ" for a in s)
print(type(ss))

sss = "".join([a if a > "A" else "QQ" for a in s])
print(sss)
#944
def deleteC(A):
    lenA  = len(A)
    lenS = len(A[0])

    cnt = 0
    for i in range(lenS):
        for j in range(lenA-1):
            if A[j][i] > A[j+1][i]:
                cnt += 1
                break
            #continue
    return cnt
#
#700
def  seaBST(root, val):
    if not root:
        return None
    elif root.val == val:
        return root
    elif root.val > val:
        return seaBST(root.left, val)
    else:
        return seaBST(root.right,val)

# 965
def isUni(root):
    if not root:
        return True
    elif root.left and root.right:
        return root.val == root.left.val == root.right.val and isUni(root.left) and isUni(root.right)
    elif root.left:
        return root.val == root.left.val and isUni(root.left)
    else:
        return root.val == root.right.val and isUni(root.right)
#1002
def commonCHars(A):
    dictList = [ Counter(i) for i in A]

    for i in set(A[0]):
        for j in range(1, len(A)):
            if i not in A[j]:
                del dictList[0][i]
                break
            dictList[0][i] = min(dictList[0][i], dictList[j][i])
    return list(dictList[0].elements())
def commonCHars1(A):
    dictList = [ Counter(i) for i in A]

    for i in set(A[0]):
        for j in range(1, len(A)):
            if i not in A[j]:
                del dictList[0][i]
                break
            dictList[0][i] = min(dictList[0][i], dictList[j][i])
    a_list = dictList[0].most_common()
    print(type(dictList[0].most_common()))
    print("dictList[0].most_common()", a_list)
    b_list = dictList[0].elements()
    print("dictList[0].elements()", type(b_list))
    print("dictList[0].elements()", list(b_list))
    dd = dict(dictList[0].most_common())
    print(type(dd), dd)

    print("*"*10)
    cnter = dictList[0]
    print(cnter.items())
    print(cnter.values())

    it_a = dictList[0].elements()
    while True:
        try:
            print(next(it_a))
        except:
            print("end of iterator it_a")
            break
commonCHars1(b)
###

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
print(type(list_c))

for j in list_c:
    print(j[0], j[1])
    print("*")

print("hold")

list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three', 'six']

test = zip(list1, list2)  # zip the values

testList = list(test)

a, b = zip( *testList )
print('The first list was ', list(a));
print('The second list was ', list(b));

###
#617
def mgebt(t1,t2):
    root = listNode(0)
    if not t1 and not t2:
        return None
    if t1:
        root.val += t1.val
    if t2:
        root.val += t2.val
    if t1 and t2:
        root.left  = mgebt(t1.left, t2.left)
        root.right = mgebt(t1.right, t2.right)
    elif t1:
        root.left  = mgebt(t1.left, None)
        root.right = mgebt(t1.right, None)
    else:
        root.left  = mgebt(None, t2.left)
        root.right = mgebt(None, t2.right)
    return root
#

print(abc(a,b))
class a():
    dd = 100
    print("dd is {}".format(dd))
    def test(self):
        print("self.dd is ", self.dd)
        # print("how about dd is ", dd)


aa = a()
aa.test()
# print("a.dd is " a.dd)
class Shark:

    # Class variables
    animal_type = "fish"
    location = "ocean"

    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method with instance variable followers
    def set_followers(self, followers):
        print("This user has " + str(followers) + " followers")
bbb = Shark("jack",100)
bbb.animal_type="Mammel"
ccc = Shark("peter", 3)
print(ccc.animal_type)

print(time.time())
print(round(time.time()))
print(round(time.time()*1000))
#944


