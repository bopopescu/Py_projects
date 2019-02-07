list_a = [1, 2, 3, 4]
#list_a.clear()

del list_a[:]
print(list_a)

wd = "Wifi test, 11ax"
print(len(wd))
print(wd.find("11ax", 10, 14))

wd = wd.replace("Wk", "AX")
print(wd)