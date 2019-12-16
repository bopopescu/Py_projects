def test_passing():
    assert (1, 2, 3) == (1, 2, 3)
    print('test file name is __file__"')


from collections import namedtuple

test_item = namedtuple("wifi", ['bandwidth', 'freq', 'rate'])
new_test = test_item(80, 5810, "MCS0")

# print("bandwidth is {0}, freq is {1}, and rate is {2}".format(new_test.bandwidth, new_test.freq, new_test.rate))

print("bandwidth is {}, freq is {}, and rate is {}.".format(*new_test))
     
