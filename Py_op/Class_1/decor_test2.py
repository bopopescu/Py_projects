from time import time, sleep

# test.1
def f():
    sleep(.3)

def g():
    sleep(.8)


# No decorator
def measure_diff(func_obj):
    st = time()
    func_obj()
    print(func_obj.__name__, " took ", "{:.1f}".format(time() - st))


# measure_diff(f)
# measure_diff(g)

# test.2
def ff(sleep_time=0.1):
    sleep(sleep_time)


def measure_diff_ff(func_obj, *args, **kwargs):
    t = time()
    func_obj(*args, **kwargs)
    print("{} took {:.1f}".format(func_obj.__name__, time() - t))

    # measure_diff_ff(ff, 0.2)
    # measure_diff_ff(ff, sleep_time=0.3)
# ff took 0.2
# ff took 0.3


# test.3
def fff(sleep_time=0.1):
    sleep(sleep_time)


def measure_decorator(func_object):
    def wrapper(*args, **kwargs):
        t = time()
        func_object(*args, **kwargs)
        print("{} through decorator took {:.1f}".format(func_object.__name__, time() - t))
    return wrapper

# test.4
def measure_decorator_1(func_object):
    def wrapper(*args, **kwargs):
        t = time()
        func_object(*args, **kwargs)
        print("{} through decorator took {:.1f}".format(func_object.__name__, time() - t))
    return wrapper

@measure_decorator_1
def ffff(sleep_time=0.1):
    sleep(sleep_time)



# ***********************************************
if __name__ == "__main__":
    measure_diff(f) # f took 0.3
    measure_diff(g) # f took 0.8
    print("______________________________________")
    measure_diff_ff(ff, 0.2)
    measure_diff_ff(ff, sleep_time=0.3)
    print("======================================")
    print("calling decorator")
    fff = measure_decorator(fff) # decoration point
    fff(.5)
    print("**************************************")
    ffff(2)
    ffff(sleep_time=4)