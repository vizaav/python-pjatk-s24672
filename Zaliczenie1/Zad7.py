"""
 Zadanie 7 - 4 pkt
--------------------------------------------------------------------------------
Napisz skrypt wyświetlający wszystkie liczby całkowite z przedziału od 20 do 80
podzielne przez dowolną liczbę k, którą podaje użytkownik. Liczby powinny być
wyświewtlone w postaci listy lub słownika. Decyduje użytkownik skryptu
"""
k = int(input("Podaj liczbę k: "))
choice = input("Wybierz listę (l) lub słownik (s): ")
if choice == "l":
    container = []
else:
    container = {}
for i in range(20, 81):
    if i % k == 0:
        if choice == "l":
            container.append(i)
        else:
            container[i] = i
print(container)
