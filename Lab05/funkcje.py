"""
Funkcje
"""


def wyswietl(a, b):
    print(a, b)


wyswietl(2, 1)


def dodaj(a, b):
    return a + b


wyswietl(dodaj(1, 2), dodaj(3, 4))


# funkcje wewnetrzne
def funkcja1(a):
    print(a)

    def funkcja2():
        print(a * 2)

    funkcja2()


funkcja1(5)


def oblicz(a, b):
    print(a * b)


test = oblicz  # alias
test(2, 3)

a = 10

if a < 5:
    def funkcja():
        print("Liczba mniejsza od 5")
else:
    def funkcja():
        print("Liczba wieksza lub rowna 5")

funkcja()

"""
argumenty funkcji
"""


# przyklad 1

def wyswietl(a, b, c):
    print(a, b, c)


wyswietl(1, 2, 3)
wyswietl(1, c=2, b=3)


# przyklad 2
def wyswietl2(a, b=4, c=8):
    print(a, b, c)


wyswietl2(1)
wyswietl2(1, 2)
wyswietl2(1, 2, 3)


# argumenty dowolne

def wypisz(*arg):  # dowolne, oprocz list i slownikow
    print(arg)


wypisz(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def wypisz2(**arg):
    print(arg)


wypisz(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
wypisz2(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10)


# kolejnosc argumentow
def wypisz3(a, b, c=3, *arg, **kwargs):
    print(a, b, c, arg, kwargs)


wypisz3(1, 2)
wypisz3(1, 2, 3, e=5, f=6, g=7, h=8, i=9, j=10)


