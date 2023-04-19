"""
Lab07 - metody
"""
class Zwierz:
    """Pierwsza klasa"""
    rodzaj = "Zwierze"
    zwierzeta = {}

    def ___init___(self, gatunek, wiek, predkosc):
        self.gatunek = gatunek
        self.wiek = wiek
        self.max_predkosc = predkosc
        if gatunek in Zwierz.zwierzeta:
            Zwierz.zwierzeta += 1
        else:
            Zwierz.zwierzeta[gatunek] = 1
    def oblicz_odleglosc(self, czas):
        print(czas * self.max_predkosc)

    @staticmethod
    def wypisz_zwierzeta():
        print(Zwierz.zwierzeta)

Zwierz.wypisz_zwierzeta()
a = Zwierz("lis", 5, 10)
b = Zwierz("python", 2, 5)
c = Zwierz("lis", 3, 10)

a.oblicz_odleglosc(2)
b.oblicz_odleglosc(2)



