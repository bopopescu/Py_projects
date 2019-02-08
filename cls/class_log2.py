class MyClass:
    element1 = "Hello"

    def __init__(self):
        self.element2 = "World"

obj = MyClass()
s_obj = MyClass()

print (dir(MyClass))
print (dir(obj))
obj.x = 100
print(obj.x)
#print(s_obj.x)#AttributeError: 'MyClass' object has no attribute 'x'
print(dir(obj))

"""

 
print dir(obj)
print "--"
print obj.element1 
print obj.element2
print MyClass.element1 + " " + MyClass.element2
"""