from collections import deque

# 1. input : iterable or empty deque
dq = deque("iterable")
dq = deque()

# newdq = deque(100) TypeError: 'int' object is not iterable

s = "a"

# 2. basic functions
dq.append(s)
dq.appendleft(s)

dq.pop()
dq.popleft()

dq.clear() # remove all elements

dq.count(s)  # count # of elemet == s

dq.extend(iterable="abcd")
dq.extendleft(iterable="dcba")



