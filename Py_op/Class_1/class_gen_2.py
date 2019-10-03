# class attribute
class InstanceCounter:
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1
        #count +=1  , wrong

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(5)
print("val of obj: {0}, count: {1}".format(a.get_val(), a.get_count()))

b = InstanceCounter(10)
print("val of obj: {0}, count: {1}".format(b.get_val(), b.get_count()))

c = InstanceCounter(100)
print("val of obj: {0}, count: {1}".format(c.get_val(), c.get_count()))

"""
val of obj: 5, count: 1
val of obj: 10, count: 2
val of obj: 100, count: 3
"""

print(c.count, InstanceCounter.count) # 3, 3
c.count = 10
print(c.count, InstanceCounter.count) # 10, 3
