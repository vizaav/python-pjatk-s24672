"""
lab01 - przywitanie z pythonem
"""
#wyświetlenie tekstu
print("Witaj, Python!")


#podstawowe formatowanie tekstu (Python 2.7)
print("Mam na imię %s. Mam %d lat. " % ("Mark", 5))

#Podstawowe formatowanie tekstu Python 3.x
print("Mam na imię {0}. Mam {1} lat".format("Mark", 5))

# input("Ile masz lat? \n")

zm = 10;
print(zm)
zm = 10 + 1
print(zm)
zm = "Napis"
print(zm)
# zm = "Eksperyment" + 1
print(zm)


#deklaracja wielu zmiennych
a, b, c = 1, 2, 3
print(c)
k = (2, 4, 6)
(x, y, z) = k
print(x)

#usuwanie zmiennych
del x
x = "ur mom"
print(x)

