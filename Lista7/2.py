import random

def generuj_liste():
    try:
        zakres = int(input("Podaj zakres generowanych liczb: "))
        ilosc = 20
        opcja = input("Czy chcesz podać liczby samodzielnie? (T/N): ")

        if opcja.lower() == 't':
            lista = []
            for i in range(ilosc):
                liczba = int(input(f"Podaj liczbę {i+1}/{ilosc}: "))
                lista.append(liczba)
        else:
            lista = random.sample(range(zakres + 1), ilosc)

        return lista
    except ValueError:
        print("Wprowadzono niepoprawne dane.")

# Przykład użycia
lista = generuj_liste()
print("Wygenerowana lista:", lista)
