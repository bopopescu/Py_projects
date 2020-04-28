s = '123'
a = s.split()
# ['123']

b = list(s)
# ['1', '2', '3']

# c = s.split('') # ValueError: empty separator

a = [3,2,0, 6, 1,4,5]

# Does Not work
a[0:4].sort()  # sort() Returns a Nonstype, Not a list
# print(a)  [3, 2, 0, 6, 1, 4, 5]

# works
a[0:4] = sorted(a[0:4])
# [0, 2, 3, 6, 1, 4, 5]
print(a)

# Error
# a[0:4] = a[0:4].sort() TypeError: can only assign an iterable

# string to list
s = "abc"
s_list = list(s)
s_list = [ch for ch in s]

# list to string
# make sure each element in list is a string
# otherwise, type error
ss = "".join(s_list)

s_lst = ['a', 'b',10, 'c']
# s_str = "".join(s_lst)
# TypeError: sequence item 2: expected str instance, int found

# Maximal positive 32-bit number is 0x7FFFFFFF = (1<<31) - 1 =2147483647
(1 << 31) -1
# The minimal number in two's complement notation is 0x80000000 = -2147483648

# max: \
float('inf')
# min: \
float('-inf')

# strs1_st = sorted(strs1, key=len)

res = []
def mod(res):
    res = [1,2,3]
mod(res)
# print(res) []

#
res = []
def mod(res):
    res += [1, 2, 3]

mod(res)
print(res)  # [1, 2, 3]

#
res = []
def mod(res):
    c = [1,2,3]
    res += c

mod(res)
print(res)  # [1, 2, 3]

# 842. Split Array into Fibonacci Sequence
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        # 5:33 4/22

        def splitArray(S, ind, ans, res):
            if ind == len(S) and len(ans) > 2:
                res += ans
                return
            for i in range(ind, len(S)):
                p = S[ind:i + 1]
                if int(p) > (1 << 31) - 1:
                    break
                elif len(p) > 1 and p[0] == "0":
                    break;
                if len(ans) >= 2:
                    if int(ans[-2]) + int(ans[-1]) > int(p):
                        continue
                    elif int(ans[-2]) + int(ans[-1]) < int(p):
                        break
                ans.append(p)
                splitArray(S, i + 1, ans, res)
                if res:
                    break
                ans.pop()

        res = []
        splitArray(S, 0, [], res)
        return res

arr = [0,1,2,3,4,5]

for i in range(len(arr)):
    print(i)
    if arr[i] > 1:
        i = 4

    print("----", i)

# 0
# ---- 0
# 1
# ---- 1
# 2
# ---- 4
# 3
# ---- 4
# 4
# ---- 4
# 5
# ---- 4


