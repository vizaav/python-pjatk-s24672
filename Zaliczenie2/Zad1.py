"""
Napisz skrypt, który pobierze od użytkownika 3 liczby całkowite i w odpowiedzi na
ekranie wyświetli liczbę gwizdek, # i $ np.:
* # $
* # $
* #
*
*
Każdy znak to osobna kolumna. Zastosuje odpowiednie formatowanie
"""
liczba1 = int(input("Podaj pierwszą liczbę całkowitą: "))
liczba2 = int(input("Podaj drugą liczbę całkowitą: "))
liczba3 = int(input("Podaj trzecią liczbę całkowitą: "))

liczby = [liczba1, liczba2, liczba3]

for i in range(max(liczby)):
    t_print = ""
    if i < liczby[0]:
        t_print += "*\t"
    else:
        t_print += " \t"
    if i < liczby[1]:
        t_print += "#\t"
    else:
        t_print += " \t"
    if i < liczby[2]:
        t_print += "$"
    else:
        t_print += " "
    print(t_print)
