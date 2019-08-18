#
# from boltons.funcutils import wraps
#
# def decorator(some_function):
#     @wraps(some_function)
#     def wrapper():
#         print("This is printed before call the function.")
#         some_function()
#         print("This is printed after call the function.")
#     return wrapper
#
# def my_function():
#     print("This is the function!")
#
# my_function = decorator(my_function)
#
# my_function()
#
# def decorator1(func):
#     def wrapper():
#         print("First Function")
#         func()
#         print("End of Function")
#     return wrapper
#
# def test_func():
#     print("this is test_func")
# print("\n\n")
#
# #test_func = decorator1(test_func)
#
# test_func()


def decorator3(func):
    def wrapper():
        print("First Function")
        func()
        print("End of Function")
    return wrapper

@decorator3
def test_func():
    print("this is test_func")

test_func()


# pass function with parameters
# def func_called(func):
#     def wrapper():
#         print("func_called is called!")
#         print("func is called ".format(func()))
#     return wrapper()
#
#
# @func_called
# def foo(a,b):
#     print("foo is called!")
#     return a+b
#
# foo(100,200)

print("________________Python decorator 1 _____________")


# Python program to explain property()
# function using decorator

class Alphabet:
    def __init__(self, value):
        self._value = value

    # getting the values
    @property
    def value(self):
        print('Getting value')
        return self._value

    # setting the values
    @value.setter
    def value(self, value):
        print('Setting value to ' + value)
        self._value = value

    # deleting the values
    @value.deleter
    def value(self):
        print('Deleting value')
        del self._value

    # passing the value


x = Alphabet('Peter')
print(x.value)

x.value = 'Diesel'

del x.value

print("________________End of Python decorator 1 _____________")

print("________________Python decorator 2 _____________")


# Python program to explain property() function

# Alphabet class
class Alphabet:
    def __init__(self, value):
        self._value = value

        # getting the values

    def getValue(self):
        print('Getting value')
        return self._value

        # setting the values

    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value

        # deleting the values

    def delValue(self):
        print('Deleting value')
        del self._value

    value = property(getValue, setValue, delValue, )


# passing the value
x = Alphabet('GeeksforGeeks')
print(x.value)

x.value = 'GfG'

del x.value

print("________________End of Python decorator 2 _____________")

print("\n\n________________Python decorator 3 _____________")

class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @full_name.setter
    def full_name(self, value):
        first_name, last_name = value.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @full_name.deleter
    def full_name(self):
        del self.first_name
        del self.last_name

worker = Person("Jeffery", "Epstain")
print("worker's full name is {}".format(worker.full_name))
worker.full_name = "Gelain Maxwell"
print("worker's full name is {}".format(worker.full_name))


print("________________End of Python decorator 3 _____________")