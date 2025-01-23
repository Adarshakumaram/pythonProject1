from os import remove
from queue import PriorityQueue

from numpy.testing.print_coercion_tables import print_new_cast_table

a=[1,2,3]
print(a)
a.append(334)
print(a)
a.extend([4,5,6])
print(a)
a.insert(1,"adhu")
print(a)
print(len(a))
a.remove(5)
print(a)

print("------")
b=a.copy()
print(b)

a.remove("adhu")
a.sort()
print(a)
print(a.pop())
print(a)