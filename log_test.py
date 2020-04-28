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

