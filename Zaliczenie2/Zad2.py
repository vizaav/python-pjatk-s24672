"""
 Napisz skrypt, który będzie działał jak prosty kalkulator (obsługa dodawania,
odejmowania, mnożenia, dzielenia, dzielenia bez reszty, %, pierwiastek kwadratowy,
pierwiastek dowolnego stopnia, potęga)
"""
import math


def dodawanie(a, b):
    # +
    return a + b


def odejmowanie(a, b):
    # -
    return a - b


def mnozenie(a, b):
    # *
    return a * b


def dzielenie(a, b):
    # /
    return a / b


def dzielenie_bez_reszty(a, b):
    # //
    return a // b


def modulo(a, b):
    # %
    return a % b


def pierwiastek_kwadratowy(a):
    # sqrt
    return math.sqrt(a)


def pierwiastek_dowolnego_stopnia(a, b):
    # root
    return a ** (1 / b)


def potega(a, b):
    # pow
    return a ** b


znaki = {"+": dodawanie, "-": odejmowanie, "*": mnozenie, "/": dzielenie, "//": dzielenie_bez_reszty, "%": modulo,
         "sqrt": pierwiastek_kwadratowy, "root": pierwiastek_dowolnego_stopnia, "pow": potega}


def kalkulator():
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    choice = input("Wybierz działanie: +, -, *, /, //, %, sqrt, root, pow: ")
    liczba2 = float(input("Podaj drugą liczbę: "))
    print(f"{liczba1} {choice} {liczba2} = {znaki[choice](liczba1, liczba2)}")
    kontynuacja = input("Czy chcesz kontynuować? (t/n): ")
    if kontynuacja == "t":
        looping = True
        while looping:
            liczba1 = znaki[choice](liczba1, liczba2)
            choice = input("Wybierz działanie: +, -, *, /, //, %, sqrt, root, pow: ")
            liczba2 = float(input("Podaj drugą liczbę: "))
            print(f"{liczba1} {choice} {liczba2} = {znaki[choice](liczba1, liczba2)}")
            kontynuacja = input("Czy chcesz kontynuować? (t/n): ")
            if kontynuacja == "n":
                break


kalkulator()
