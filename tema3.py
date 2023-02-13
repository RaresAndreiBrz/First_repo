

"""
#Live 1
lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = ["apple", "MACC", "iphone", "ipad", "apple"]
lista_3 = [1, True, "_", False, 5.2 ]
lista_matrice = [lista_1, lista_2, lista_3]
lista_mare = [lista_matrice, [0, 1, lista_1, ["a","b", "c"], [lista_matrice]], {}, True]

#sortati lista 2 dupa penultimu caracter din fiecare string din lista
#Live 1
#sortati lista 2 dupa penultimu caracter din fiecare string din lista
ista_2 = ["apple", "macc", "iphone", "ipad", "apple"]
lista_2.sort(key=lambda x: x[-2])
print(lista_2)


#numarti cate elem sunt intr o lista mai mult decat o data, cu elim spatiilor, litera mare , si semne punctuatie
numaratoare1 = lista_2.count("apple")
print(numaratoare1)
import string
alphabet = list(string.ascii_uppercase)
alphabet_as_set = set(alphabet)
intersection = alphabet_as_set.intersection(lista_mare)
numaratoare2 = list(intersection)
print(numaratoare2)
"""



############################################################################################################
#TEMA OBLIGATORIE

#Ex1
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

#Ex2
print(note_muzicale.count("do"))

#Ex3
listaCifre1 = [3, 1, 0, 2]
listaCifre2 = [6, 5, 4]
listaCifre_total = listaCifre2 + listaCifre1
listaCifre_total2 = []
listaCifre_total2.extend(listaCifre1)
listaCifre_total2.extend(listaCifre2)
print(listaCifre_total2)
print(listaCifre_total)

#Ex4

listaCifre_total2.remove(0)
print(listaCifre_total2)

#Ex5

if len(listaCifre_total2) == 0:
    print("Lista e goala.")
else:
    print("Lista nu este goala")

#Ex 6
listaCifre_total2 = []
print(listaCifre_total2)

#Ex 7
if len(listaCifre_total2) == 0:
    print("Lista e goala.")
else:
    print("Lista nu este goala")

#Ex 8
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

#Ex 9
print("Ana a luat nota " + str(dict1.get('Ana')))
print("Gigel a luat nota " + str(dict1.get('Gigel')))
print("Dorel a luat nota " + str(dict1.get('Dorel')))

#Ex 10
dict1['Dorel'] = 6
print(dict1['Dorel'])

#Ex 11
del dict1['Gigel']
print(dict1)
dict1['Ionica'] = 9
print(dict1)

#Ex 12
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)
#nu a fost adaugat itemul de la linia 100

#Ex 13
print(weekend.issubset(zile_sapt))

#Ex 14
diferenta1 = zile_sapt.difference(weekend)
diferenta2 = weekend.difference(zile_sapt)
print(diferenta1)
print(diferenta2)

#Ex 15
elem_comune = set(weekend.intersection(zile_sapt))
print(elem_comune)

######################################################################
# Ex cu optionalul e intr-un alt fisier