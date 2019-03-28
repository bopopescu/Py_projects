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