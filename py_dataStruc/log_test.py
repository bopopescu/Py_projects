test = dict([('wifi', 2),("bt",3),('AC',4)])

test_1 = [("mu",5),("su",6),("su", 7)]

test.update(test_1)

print(type(test.items()))
test2 = list(test.items())
for i in test2:
    print(i, sep="; ")