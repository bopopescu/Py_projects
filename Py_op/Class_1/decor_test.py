def smart_divide(calling_func):
    def inner(a, b):
        print("inner(a, b) call {} divide {}".format(a,b))
        if b == 0:
            print("Whoops! cannot divide")
            return
        return calling_func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return a/b


if __name__ == "__main__":
    print(divide(10, 2))
    print(divide(10, 0))

    """
    I am going to divide 10 and 2
5.0
I am going to divide 10 and 0
Whoops! cannot divide
None

    """
