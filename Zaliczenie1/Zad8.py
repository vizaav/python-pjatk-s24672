"""
 Zadanie 8 - 4 pkt
--------------------------------------------------------------------------
Zmodyfikuj zadanie 7 w taki sposób, aby użytkownik mógł podać zakres liczb
oraz ilość dowolnych liczb k.
Wyniki wyświetl w postaci słownika (k: liczby całkowite)
"""
bottom = int(input("Podaj dolny zakres: "))
top = int(input("Podaj górny zakres: "))
number_of_k = int(input("Podaj ilość liczb k: "))
dictionary = {}
for i in range(number_of_k):
    k = int(input("Podaj liczbę k: "))
    container = []
    for i in range(bottom, top + 1):
        if i % k == 0:
            container.append(i)
    dictionary[k] = container
print(dictionary)



