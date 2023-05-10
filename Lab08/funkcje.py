"""
Lab08 - użycie własnego modułu
"""
import math
import sys


def oblicz_pole_kola(promien):
    return math.pi * promien ** 2



def oblicz_obwod_kola(promien):
    return 2 * math.pi * promien


def main():
    print(sys.argv)
    print(oblicz_obwod_kola(int(sys.argv[1])))


if __name__ == '__main__':
    main()
