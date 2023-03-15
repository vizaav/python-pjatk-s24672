"""
Lab02 - operacje na łańcuchach i konwersja typów
"""
napis = "Wiek: " + str(10)
print(napis)

# zmiana znaków w tekście
print(napis.replace("W", "w"))
print(napis.upper())
counter = 0
for letter in napis:
    if (counter % 2 == 0):
        print(letter.upper(), end="")
        counter = counter + 1
    else:
        print(letter.lower(), end="")
        counter = counter + 1

# konwersja typu tekstowego na typ liczbowy
a = '5'
b = 7
print(int(a) + b)

# konwersja typu liczbowego na typ tekstowy
a = '6'
b = 9
print(a + repr(b))
print(a + str(b))

# operatory wyrażeń boolean
x = 2
y = 4
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)
print(x == y)
print(x != y)
print()
print(a or b)
print(a and b)
print(not a)
print(not b)

# operatory arytmetyczbe'
a, b = 2, 3
print(a + b)
print(a - b)
print(a * b)
print(a/b)
print(a % b)
print(a ** b)

#zmiana wartosci zmiennych
a, b, c, d = 1, 3, 7, 4
a+=2
b -= 2
c *= 2
d /= 2
print(a, b, c , d)
