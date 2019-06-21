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

print(return_value_and_None()) # None


