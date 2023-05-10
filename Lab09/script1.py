"""
Lab 09 - obsługa plików, odczyt
"""

# Metoda 1

plik1 = open('czarny_kot', mode='r', encoding='utf-8')
tresc = plik1.read()
print(tresc)
plik1.close()
print(plik1.closed)

# Metoda 2
plik2 = open('czarny_kot', mode='r', encoding='utf-8')
print(plik2.readline())
plik2.close()

# Metoda 3
plik3 = open('czarny_kot', mode='r', encoding='utf-8')
for linia in plik3:

    if linia == "\n":
        print('Chwała Polsko-Japońskiej Akademii Technik Komputerowych!')
    else:
        print(linia)

plik3.close()

# Metoda 4
with open('czarny_kot', mode='r', encoding='utf-8') as plik4:
    print(plik4.read())
