"""
Lab09 - wyjątki
"""


def pobierz(sek, ind):
    return sek[ind]


pliki = ["czarny_kot.txt", "nowy_plik.txt"]
ind = 2
try:
    print(pobierz(pliki, ind))
except IndexError as e:
    print(e)
    print("Nie ma takiego indeksu")

pliki = ["czarny_kot.txt", "nowy_plik.txt"]
ind = 1
try:
    p = pobierz(pliki, ind)
    print(p)
    f = open(p)
except(IndexError, FileNotFoundError) as e:
    print(e)
    print("Nie ma takiego indeksu lub pliku")
else:
    print("pobrano nazwę pliku")
