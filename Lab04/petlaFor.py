"""
Lab04 - petla for
"""

# przyklad petli for
listA = ["abc", [1,2,3]]

for i in listA:
    print(i)

# for i in range(len(listaA)):
#     print(i)

for i in listA:
    print(i)
    for j in i:
        print(j)

#przyklady formatowania teksu (Python 2.7 i Python 3.x)
# for x in  range(-10, 11):
#     print("%+1" %x, end=" " )
# print("\n")

# for x in range(5, 100, 10):
#     print("%31%60%5x" %(x,x,x) )
#
#
# for x in range(5, 100, 10):
#     print("%-31%-60%-5x" %(x,x,x))
#
# #wyrownanie do lewej (x wlasciwy prefix)
# for x in range(5, 100, 10):
#     print("%-31%-60%-5x" %(x,x,x))

for x in range(5, 100, 10):
    print("%031 %#04o %#04x" % (x, x, x))

