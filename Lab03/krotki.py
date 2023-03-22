"""
Lab03 - krotki
"""

# tworzenie krotki
krotka1 = ()
print(krotka1)

krotka1 = 1
print(krotka1)

krotka1 = (1,)
print(krotka1)

krotka2 = 1, 3.14, "PJATK"

krotka3 = 1, 3.14, [2, 3], 1
print(krotka3)

napis = "abcdefg"
print(tuple(napis))


#indeksowanie krotek
print(krotka3[0])
print(krotka3[:2])

# operacje na krotkach
print(krotka3.count(1))
print(krotka3.index(3.14))


