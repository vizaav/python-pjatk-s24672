"""
Lab04 - petla while
"""

# przyklad prostej petli while
x = 0
while x < 10:
    x += 1
    print(x)

x = {1, 2, 3, 4, 5}
while x:
    print(x.pop())
else:
    print("Zbior x jest pusty")
