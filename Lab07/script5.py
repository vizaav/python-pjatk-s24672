"""
Lab07 - metody specjalne klas
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

    def __str__(self):
        return self.gatunek + "ma" + str(self.wiek) + \
               " lat i osiąga prędkość " + str(self.max_predkosc) + " km/h."

class Ptak(Zwierz):
    def __init__(self, gatunek, wiek, predkosc, max_predkosc_lotu, miejsce):
        super().__init__(gatunek, wiek, predkosc)
        self.max_predkosc = max_predkosc_lotu
        self.miejsce = miejsce

    def przenies(self):
        if self.miejsce == "Klatka":
            self.miejsce = "Otwarty"
        else:
            self.miejsce = "Klatka"
p = Ptak("pingwin", 2, 3, 0, "Otwarty")
