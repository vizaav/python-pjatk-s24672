"""
Lab08 - użycie własnego modułu
"""

import funkcje
from funkcje import oblicz_obwod_kola

pole = funkcje.oblicz_pole_kola(4)
print(pole)
obwod = oblicz_obwod_kola(4)
print(obwod)

# pakiety

import przykladowy_pakiet.funkcje as f

pole = f.oblicz_pole_kola(4)
print(pole)
