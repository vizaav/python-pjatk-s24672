"""
Lab09 - obsługa plików, zapis
"""

plik1 = open('nowy_plik.txt', mode='w', encoding='utf-8')
plik1.write('Pierwsza linia\n')
plik1.close()

plik2 = open('nowy_plik.txt', mode='a', encoding='utf-8')
p1 = plik2.write('Druga linia\n')
plik2.close()
print(p1)

plik3 = open('nowy_plik.txt', mode='a', encoding='utf-8')
plik3.write('Trzecia linia\n')
plik3.close()

with open('nowy_plik.txt', mode='a', encoding='utf-8') as plik4:
    print(plik4.read())
