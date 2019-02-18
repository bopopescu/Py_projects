test_id = ["wifi", "ax", "bt"]

test = test_id.copy()

#test1 = test_id.copy.deepcopy()
import copy
test_1 = copy.deepcopy(test_id)

print(id(test_id), id(test), id(test_1), sep="; ")
