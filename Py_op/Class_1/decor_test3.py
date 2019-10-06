from time import time, sleep


def f():
    sleep(.3)


def g():
    sleep(.8)


# No decorator
def measure_diff(func_obj):
    st = time()
    func_obj()
    print(func_obj.__name__, " took ", time() - st)


###################
def ff(sleep_time = 0.1):
    sleep(sleep_time)


def measure_diff_ff(func_obj, *args, **kwargs):
    t = time()
    func_obj(*args, **kwargs)
    print("{0} took {1}".format(func_obj.__name__, time() - t))


################################
def fff(sleep_time = 0.1):
    sleep(sleep_time)


def measure_decorator(func_object):
    def wrapper(*args, **kwargs):
        t = time()
        func_object(*args, **kwargs)
        print("{0} through decorator took {1}".format(func_object.__name__, time() - t))
    return wrapper


if __name__ == "__main__":
    measure_diff(f)
    measure_diff(g)
    print("*"*30)
    measure_diff_ff(ff, 0.5)
    measure_diff_ff(ff, sleep_time=0.5)
    print("calling decorator")
    fff = measure_decorator(fff) #decoration point
    fff(0.5)