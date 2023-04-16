"""
Zadanie 4 - 5 pkt
---------------------------------------------------------------
Coca-Colę piją obecnie tylko zamożni obywatele. Napisz skrypt,
w którym przygotowujesz raport pokazujący zmiany cen tego
popularnego napoju po dodaniu nowego podatku cukrowego:
Ceny przed: 3.69, 4.5, 3.6, 4.0, 3.99, 3.59
Ceny po: 4.5, 5.5, 4.69, 4.99, 4.00
Twoim zadaniem jest podanie informacji o:
a) najwyższej cenie po nałożeniu podatku,
b) najniższej cenie biorąc pod uwagę wszystkie ceny (przed i po),
c) średniej cenie przed podwyżką cen,
d) średniej cenie po dodaniu nowego podatku.
"""
prices_before = [3.69, 4.5, 3.6, 4.0, 3.99, 3.59]
prices_after = [4.5, 5.5, 4.69, 4.99, 4.00]
all_prices = prices_before + prices_after
print("Najwyższa cena po podwyżce: ", max(prices_after))
print("Najniższa cena ogółem: " , min(all_prices))
print("Średnia cena przed podwyżką: ", sum(prices_before) / len(prices_before))
print("Średnia cena po podwyżce: ", sum(prices_after) / len(prices_after))
