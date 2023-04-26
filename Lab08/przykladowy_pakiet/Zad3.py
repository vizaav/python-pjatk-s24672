"""
Zadanie3(2pkt)------------------------------------------------------
Utwórz pakiet składający się z algorytmów poznanych na wcześniejszych zajęciach.
"""
import math


def oblicz_pole_kola(promien):
    return math.pi * promien ** 2


def oblicz_obwod_kola(promien):
    return 2 * math.pi * promien


def oblicz_pole_trojkata(a, h):
    return (a * h) / 2


def oblicz_pole_prostokata(a, b):
    return a * b


def oblicz_pole_prostopadloscianu(a, b, h):
    return 2 * (a * b + b * h + a * h)
