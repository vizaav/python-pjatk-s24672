"""
 Zadanie 3 - 3 pkt
---------------------------------------------------------------
Napisz skrypt rysujący z gwiazdek * prostokąt o długości a = 3
i szerokości b = 4. Spraw aby skrypt obliczał i wyświetlał pole
oraz obwód tego prostokąta.

"""
a = 3
b = 4
for i in range(a):
    print("*" * b)
print("Pole prostokąta wynosi: ", a * b)
print("Obwód prostokąta wynosi: ", 2 * a + 2 * b)