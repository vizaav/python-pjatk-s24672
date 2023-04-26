"""
Lab08
"""
import random

from random import randint


random.seed()
print(random.randint(1, 100))

l = list(range(1, 101))
print(random.choice(l))

random.shuffle(l)
print(l)

print(random.random())
print(random.uniform(10,30))
