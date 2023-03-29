"""
Lab03 - slowniki
"""
# Tworzenie slownika
x = {}
print(x)

x = dict()
print(x)

x = {"Nazwisko" : "Wolf", "Wiek" : 25}
print(x)

x = dict(Nazwisko="Wolf", Wiek=25)
print(x)

#operacje na słownikach
nazwisko = x["Nazwisko"]
print(nazwisko)

wiek = x.get("Wiek")
print(wiek)

x["Nazwisko"] = "Blue"
print(x)

nowe_elementy = {"Zawód" : "Informatyk", "Klasa" : 1}
x.update(nowe_elementy)
print(nowe_elementy)

x.pop("Klasa")
print(x)

# x.clear()
# print(x)

print(x.keys())
print(x.values())
print(x.items())



