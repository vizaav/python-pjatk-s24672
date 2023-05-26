from datetime import datetime


class Osoba:
    def __init__(self, imie, nazwisko, plec, data_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec
        self.data_urodzenia = data_urodzenia

    def wyswietl_info(self):
        return {
            'Imię': self.imie,
            'Nazwisko': self.nazwisko,
            'Płeć': self.plec,
            'Data urodzenia': self.data_urodzenia
        }

    def wylicz_wiek(self):
        data_urodzenia = datetime.strptime(self.data_urodzenia, "%d-%m-%Y")
        dzis = datetime.today()
        roznica = dzis - data_urodzenia
        wiek = roznica.days // 365
        return wiek

    @staticmethod
    def wyswietl_osoby(osoby):
        lista_osob = []
        for osoba in osoby:
            lista_osob.append(osoba.wyswietl_info())
        return lista_osob


# Tworzenie obiektów Osoba
osoba1 = Osoba("Jan", "Kowalski", "Mężczyzna", "01-01-1990")
osoba2 = Osoba("Anna", "Nowak", "Kobieta", "15-05-1985")

# Wywołanie metody wyswietl_info dla obiektów Osoba
print(
    osoba1.wyswietl_info())  # {'Imię': 'Jan', 'Nazwisko': 'Kowalski', 'Płeć': 'Mężczyzna', 'Data urodzenia': '01-01-1990'}
print(
    osoba2.wyswietl_info())  # {'Imię': 'Anna', 'Nazwisko': 'Nowak', 'Płeć': 'Kobieta', 'Data urodzenia': '15-05-1985'}

# Obliczanie wieku osoby
print(osoba1.wylicz_wiek())  # np. 33

# Wywołanie metody wyswietl_osoby dla listy obiektów Osoba
osoby = [osoba1, osoba2]
print(Osoba.wyswietl_osoby(osoby))
# [{'Imię': 'Jan', 'Nazwisko': 'Kowalski', 'Płeć': 'Mężczyzna', 'Data urodzenia': '01-01-1990'},
#  {'Imię': 'Anna', 'Nazwisko': 'Nowak', 'Płeć': 'Kobieta', 'Data urodzenia': '15-05-1985'}]
