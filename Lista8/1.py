import json

class Produkt:
    def __init__(self, nazwa, cena, ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc

    def wyswietl_info(self):
        return {
            'Nazwa': self.nazwa,
            'Cena': self.cena,
            'Ilość': self.ilosc
        }

class BazaDanych:
    def __init__(self, plik):
        self.plik = plik
        self.produkty = []

    def dodaj_produkt(self, produkt):
        self.produkty.append(produkt)

    def usun_produkt(self, nazwa):
        for produkt in self.produkty:
            if produkt.nazwa == nazwa:
                self.produkty.remove(produkt)
                break

    def zapisz_baze(self):
        try:
            with open(self.plik, 'w') as plik:
                lista_produktow = [produkt.wyswietl_info() for produkt in self.produkty]
                json.dump(lista_produktow, plik)
                print("Baza danych została zapisana do pliku.")
        except IOError:
            print("Wystąpił błąd podczas zapisu do pliku.")

    def wczytaj_baze(self):
        try:
            with open(self.plik, 'r') as plik:
                lista_produktow = json.load(plik)
                self.produkty = [Produkt(p['Nazwa'], p['Cena'], p['Ilość']) for p in lista_produktow]
                print("Baza danych została wczytana z pliku.")
        except FileNotFoundError:
            print("Plik bazy danych nie istnieje.")
        except IOError:
            print("Wystąpił błąd podczas wczytywania pliku.")

    def wyswietl_baze(self):
        for produkt in self.produkty:
            print(produkt.wyswietl_info())

# Przykład użycia
baza = BazaDanych('baza_produktow.json')

# Wczytanie bazy danych z pliku (jeśli istnieje)
baza.wczytaj_baze()

# Dodanie produktów
baza.dodaj_produkt(Produkt("Książka", 29.99, 10))
baza.dodaj_produkt(Produkt("Telefon", 999.99, 5))
baza.dodaj_produkt(Produkt("Komputer", 1999.99, 3))

# Wyświetlenie bazy danych
baza.wyswietl_baze()

# Usunięcie produktu
baza.usun_produkt("Telefon")

# Zapisanie bazy danych do pliku
baza.zapisz_baze()
