"""
Lab07 - inicjalizowanie klas i atrybuty klas
"""

class Zwierz:
    """Pierwsza klasa"""
    rodzaj = "Zwierze"

    def ___init___(self, gatunek, wiek):
        self.gatunek = gatunek
        self.wiek = wiek


    def podaj_gatunek(self):
        print("lis")

a = Zwierz("lis", 5)
b = Zwierz("python", 2)

print(a.gatunek, a.wiek)
print(b.gatunek, b.wiek)

# definiowanie atrybutów poza klasą
b.dlugosc = 10
print(b.dlugosc)

# wyswietlanie atrybutow wspolnych dla obu klas
print(a.rodzaj, b.rodzaj)
print(Zwierz.rodzaj)

# zmiana wartości atrybutów
b.dlugosc = 11
print(b.dlugosc)
a.wiek = 6
print(a.wiek)

# atrybuty klasy w formie słownika
print(a.__dict__)
print(b.__dict__)

# opis klasy
print(Zwierz.__doc__)
print(a.__doc__)

