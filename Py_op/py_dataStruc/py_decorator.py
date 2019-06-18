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