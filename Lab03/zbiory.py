"""
Lab03 - zbiory
"""

# tqorzenie zbioru
zb1 = {1, 2}
print(zb1)

zb = {1, 2, 3}
print(zb1)

zb2 = {1, 2, 4}
print(zb2)

print(zb2.pop())
print(zb2)

# operacje na zbiorach
# print(zb1.union(zb2))
# print(zb1 | zb2)

# print(zb1.intersection(zb2))
print(set(zb1) & set(zb2))

print(zb2.difference(zb2))
print(zb1 - zb2)

print(zb1.symmetric_difference(zb2))
print(zb1 ^ zb2)

zb3 = {1, 4, 7, 3.14}
print(zb3)

zb3.add(6.18)
zb3.remove(3.14)
print(zb3)




