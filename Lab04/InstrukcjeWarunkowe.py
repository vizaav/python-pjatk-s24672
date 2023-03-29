"""
Lab04 - istrukcje warunkowe
"""

# przyklady instrukcji warunkowych

if 1 < 2:
    print("Prawda")
if True:
    print("Prawda")
if "napis":
    print("Prawda")
if 1:
    print("Prawda")
if None:
    print("Prawda")
x = True
y = False

if x and y:
    print("Prawda")
if x or y:
    print("Prawda")

# Przykład zagnieżdżonej instrukcji warunkowej
a = -1

if a < 0:
    print("Czerwony")
    if a != -20:
        print("Bingo!!!" * 3)

wybor = int(input("daj"))
if wybor < 0:
    print("Czerwony")
elif wybor == 0:
    print("Bialy")
else:
    print("Zielony")

if wybor     < 0:
    print("Czerwony")