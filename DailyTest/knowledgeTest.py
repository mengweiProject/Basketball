"""


"""

from copy import copy, deepcopy


dict1 = {"a": 123, "b": 456}
l1 = []
l1.append(dict1)
# print(l1)
l2 = l1.copy()
# print(l2)
dict1["b"] = 789
# print(l2)
# print(l1)

l3 = deepcopy(l1)
print(l3)
dict1["c"] = 111222333
print(l1)
print(l3)


