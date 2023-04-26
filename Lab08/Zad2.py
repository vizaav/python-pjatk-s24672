"""
Zadanie2(1pkt)------------------------------------------------------
Zmodyfikuj zadanie z listy nr1 dotyczące stworzenia listy z20elementóww taki spoób aby można było wygenerować losową
listę z ustalonego zakresu␣, (zakres pozostaje taki jak w zadaniu).Użytkownik powinien mieć wybór czy chce sam podać
 czy skorzystać z␣, automatu.
"""
import random

def losuj_liste(ile, zakres):
    lista = []
    for i in range(ile):
        lista.append(random.randint(1, zakres))
    return lista

def main():
    wybor = input("Czy chcesz sam podać zakres? (t/n): ")
    if wybor == "t":
        ile = int(input("Podaj ile liczb: "))
        zakres = int(input("Podaj zakres: "))
        print(losuj_liste(ile, zakres))
    else:
        print(losuj_liste(20, 100))

if __name__ == '__main__':
    main()