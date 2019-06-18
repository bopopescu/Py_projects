import random
some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("An error")

except ValueError:
    print("Caught a ValueError")
except TypeError:
    print("Caught a TypeError")
except TypeError:
    print("Caught a TypeError")
except Exception as e:
    print("Caught some other error {}".format(e.__class__.__name__)) # e.args

else: # Execute only when there is no exception caught
    print("This code called if there is no exception")

finally:
    print("This cleanup code is always called!")

