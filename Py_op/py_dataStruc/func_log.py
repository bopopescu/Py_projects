def check():
    pass

if check() is None:
    print("check() is ", check())
# check() is  None

def return_value_and_None():
    a = 10
    if a == 1:
        return a
    else:
        #return None
        pass # Same 

print("return_value_and_None() is {}".format(return_value_and_None())) # None

###
def mul(*arg):
    print("arg[0] is {}".format(arg[0]))
    for i in arg:
        print(i, end=", ")
    print()
    for i in range(len(arg)):
        print(arg[i], end=", ")

arg = (1,2,4) # arg[0] is (1, 2, 4)

# mul(1,2,4)  arg[0] is 1
mul(7,8,9)
# 7, 8, 9,
# 7, 8, 9,


