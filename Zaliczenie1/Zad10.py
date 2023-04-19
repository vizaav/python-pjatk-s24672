"""
 Zadanie 10 - 3 pkt
-------------------------------------------------------------------------------
Napisz skrypt, który korzystając z instrukcji while, sumuje liczby nieparzyste
w przedziale od 1 do 100.

"""
a = 1
suma = 0
while a <= 100:
    if a % 2 != 0:
        suma += a
    a += 1
print("Suma liczb nieparzystych w przedziale od 1 do 100: " + str(suma))
