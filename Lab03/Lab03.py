"""
Lab03 - listy
"""

# tworzenie listy
lista1 = []
print(lista1)

lista1 = [1, 2, 3]
print(lista1)

lista2 = [1, 3.14, "PJATK"]
print(lista2)

lista3: list[int] = [3, 4, 5]
print(lista3)

lista4 = [8, 6, 4]
print(lista4)

napis = "abcdef"
lista5 = list(napis)
print(lista5)

# indeksowanie list
print(lista1[0])
print(lista1[-1])
print(lista1[0:2])
print(lista1[:2])
print(lista1[1:])
print(lista5[::2])
print(lista5[::-1])
print(lista5[:len(lista5):2])

lista6 = [1, 2, [3, 4]]
print(lista6[2][0])

# modyfikowanie list
lista7 = []
lista7 = [1]
print(lista7)

lista7.append(2)
print(lista7)

lista7.insert(1, 3)
print(lista7)

lista2.remove("PJATK")
print(lista2)

lista2.pop()
print(lista2)

lista2.pop(0)
print(lista2)

lista34 = lista3 + lista4
print(lista34)

lista8 = lista3 + [8, 3, 6]
print(lista8)

lista4.extend(lista3)
print(lista4)

lista4.append(lista8)
print(lista4)

lista9 = lista1 * 3
print(lista9)

lista9.sort(reverse=True)
print(lista9)

lista9.reverse()
print(lista9)
lista10 = lista9
print(lista10)
print(lista9)

lista9[1] = 8
print(lista9)
print(lista10)
lista10 = lista9.copy()

