# Zadanie1-------------------------------------------------------
# Napisz skrypt, który będzie działał jak prosta baza produktów spożywczych.␣
# ,→Skrypt ma korzytać z klas. Zmodyfikuj kod z zadania wykonanego na jednych z poprzednich zajęć.

class ProduktSpozywczy:
    def __init__(self, nazwa, cena, ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc

    def wyswietl_informacje(self):
        print("Nazwa: ", self.nazwa)
        print("Cena: ", self.cena)
        print("Ilość: ", self.ilosc)


class BazaProduktow:
    def __init__(self):
        self.produkty = []

    def dodaj_produkt(self, produkt):
        self.produkty.append(produkt)

    def usun_produkt(self, produkt):
        self.produkty.remove(produkt)

    def wyswietl_produkty(self):
        if (len(self.produkty)) == 0:
            print("Brak produktów w bazie.")
        else:
            for produkt in self.produkty:
                produkt.wyswietl_informacje()


# Przykładowe użycie bazy produktów

# Tworzenie produktów
jogurt = ProduktSpozywczy("Jogurt", 2.50, 10)
chleb = ProduktSpozywczy("Chleb", 3.20, 5)
mleko = ProduktSpozywczy("Mleko", 2.00, 8)

# Tworzenie bazy produktów
baza = BazaProduktow()

# Dodawanie produktów do bazy
baza.dodaj_produkt(jogurt)
baza.dodaj_produkt(chleb)
baza.dodaj_produkt(mleko)

# Wyświetlanie produktów z bazy
baza.wyswietl_produkty()

# Usuwanie produktu z bazy
baza.usun_produkt(chleb)

# Wyświetlanie produktów zaktualizowanej bazy
baza.wyswietl_produkty()
