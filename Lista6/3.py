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

    @staticmethod
    def wyswietl_osoby(osoby):
        lista_osob = []
        for osoba in osoby:
            lista_osob.append(osoba.wyswietl_info())
        return lista_osob


class Gracz(Osoba):
    def __init__(self, imie, nazwisko, plec, data_urodzenia, nick, typ, email):
        super().__init__(imie, nazwisko, plec, data_urodzenia)
        self.nick = nick
        self.typ = typ
        self.email = email

    def wyswietl_info(self):
        info_osoby = super().wyswietl_info()
        info_osoby.update({
            'Nick': self.nick,
            'Typ': self.typ,
            'Email': self.email
        })
        return info_osoby

    @staticmethod
    def wyswietl_graczy(gracze):
        lista_graczy = []
        for gracz in gracze:
            lista_graczy.append(gracz.wyswietl_info())
        return lista_graczy


# Tworzenie obiektów Osoba
osoba1 = Osoba("Jan", "Kowalski", "Mężczyzna", "01-01-1990")
osoba2 = Osoba("Anna", "Nowak", "Kobieta", "15-05-1985")

# Wywołanie metody wyswietl_info dla obiektów Osoba
print(osoba1.wyswietl_info())  # {'Imię': 'Jan', 'Nazwisko': 'Kowalski', 'Płeć': 'Mężczyzna', 'Data urodzenia':
# '01-01-1990'}
print(osoba2.wyswietl_info())  # {'Imię': 'Anna', 'Nazwisko': 'Nowak', 'Płeć': 'Kobieta', 'Data urodzenia':
# '15-05-1985'}

# Wywołanie metody wyswietl_osoby dla listy obiektów Osoba
osoby = [osoba1, osoba2]
print(Osoba.wyswietl_osoby(osoby))
# [{'Imię': 'Jan', 'Nazwisko': 'Kowalski', 'Płeć': 'Mężczyzna', 'Data urodzenia': '01-01-1990'},
#  {'Imię': 'Anna', 'Nazwisko': 'Nowak', 'Płeć': 'Kobieta', 'Data urodzenia': '15-05-1985'}]

# Tworzenie obiektów Gracz
gracz1 = Gracz("John", "Doe", "Mężczyzna", "01-01-1990", "johndoe", "Premium", "johndoe@wp.pl")

# Wywołanie metody wyswietl_info dla obiektu Gracz
print(gracz1.wyswietl_info())

# Wywołanie metody wyswietl_graczy dla listy obiektów Gracz
gracze = [gracz1]
print(Gracz.wyswietl_graczy(gracze))
