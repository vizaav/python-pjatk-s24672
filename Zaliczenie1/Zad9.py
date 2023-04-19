"""
 Zadanie 9 - 3 pkt
--------------------------------------------------------------------------
Napisz skrypt, który dla trzech liczb a, b i c wprowadzonych z klawiatury
sprawdza, czy są to trójki pitagorejskie.
Dodatkowo należy założyć, że a > 0, b > 0 oraz c > 0.

"""
a, b, c = 0, 0, 0
while a <= 0 or b <= 0 or c <= 0:
    if a <= 0:
        a = int(input("Podaj liczbę a: "))
        if a <= 0:
            print("a musi być większe od 0")
    if b <= 0:
        b = int(input("Podaj liczbę b: "))
        if b <= 0:
            print("b musi być większe od 0")
    if c <= 0:
        c = int(input("Podaj liczbę c: "))
        if c <= 0:
            print("c musi być większe od 0")

if a ** 2 + b ** 2 == c ** 2:
    print("{0} + {1} = {2} - trójka pitagorejska".format(a ** 2, b ** 2, c ** 2))
else:
    print("{0} + {1} =/= {2} - nie jest to trójka pitagorejska".format(a ** 2, b ** 2, c ** 2))
