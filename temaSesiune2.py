#Ex 1
#functia IF determina drumul pe care merge codul in urma unor conditii clar definite .

#Ex 2
a = int(input("alege un numar: "))
if a > 0:
    print("a este un numar natural")
elif a == 0:
    print("a nu este numar natural pt ca nu e mai mare decat 0")
else:
    print("a nu este numar natural pt ca e mai mic decat 0")

#Ex 3
if a > 0:
    print("a este un numar pozitiv")
elif a == 0:
    print("a este numar neutru")
else:
    print("a este numar negativ")

#Ex 4
if a >= -2 and a <= 13:
    print(str(a) + " se afla in intervalul -2 / 13")
else:
    print("Nu se afla in intervalul -2 / 13")

#Ex 5
#------------------------------------------------------------------------------------nu pricep momentan

#Ex 6
x = int(input("Alege valoarea lui X: "))
if not (5 <= x <= 27):
  print("X nu se afla in intervalul dintre 5 si 27.")
else:
  print("X se afla in intervalul dintre 5 si 27.")

#Ex 7
y = int(input("Alege valoarea lui Y: "))
if x == y:
    print("Numere egale! Felicitari!")
else:
    if x > y:
        print("X este mai mare decat Y.")
    else:
        print("Y este mai mare decat X.")

#Ex 8
lat1 = int(input("Prima latime a triunghiului are lungimea (in cm): "))
lat2 = int(input("A doua latime a triunghiului are lungimea (in cm): "))
lat3 = int(input("A treia latime a triunghiului are lungimea (in cm): "))
if lat1 and lat2 and lat3 > 0:
    print("Ati ales corect lungimile")
else:
    print("Lungimile dvs nu sunt corecte. Incercati din nou cu numere pozitive va rog!")
if lat1 == lat2 == lat3:
    print("Triunghiul este echilateral ")
else:
    if lat1 == lat2 or lat2 == lat3 or lat1 == lat3:
        print("Triunghiul este unul isoscel")
    else:
        print("Triunghiul este unul oarecare")

#Ex 9
#am vrut sa fac astfel incat sa nu se blocheze codul si sa revin la inputul initial in cazul erorii acestuia.
#am folosit while loop pt asta, asa am gasit ca si varianta pt actiunea de la linia 61
while True:
    litera = input("Introduceti o litera: ").lower()
    if litera.isalpha() and len(litera) == 1:
        print("Ati introdus o litera valida:", litera)
        break
    else:
        print("Ati introdus o valoare invalida. Va rugam sa introduceti o litera: ")
        continue

if litera == "a" or litera == "e" or litera == "i" or litera == "o" or litera == "u":
    print("Ati introdus o vocala.")
else:
    print("Ati introdus o consoana.")
"""
pt a verifica atat lower cat si upper am trecut inputul direct pe lower, e in regula?
nu inteleg/ nu stiu  cum sa fac daca sterg functia lower din input. cum sa evaluez lower si upper pe parcursul codului
"""

#Ex 10
print("Ce nota ai fi luat daca dadeai BAC-ul in America?")
nota = float(input("Scrie media de la bac: "))
if nota >= 9 and nota <= 10:
    print("Nota ta este echivalenta cu nota A")
elif nota >= 8 and nota < 9:
    print("Nota ta este echivalenta cu nota B")
elif nota >= 7 and nota < 8:
    print("Nota ta este echivalenta cu nota C")
elif nota >= 6 and nota < 7:
    print("Nota ta este echivalenta cu nota D")
elif nota >= 4 and nota < 6:
    print("Nota ta este echivalenta cu nota E")
elif nota > 0 and nota < 4:
    print("Nota ta este echivalenta cu nota F")
else:
    print("Va rog nu mintiti. Incercati din nou.")

##############################################################
#Next level tema
#Ex 1

numar = str(input("Introduceti un numar din minim 4 cifre: "))
if len(numar) > 3:
    print("Ati ales corect numarul. Nu a fost asa greu.")
else:
    print("Of...te-am rugat din minim 4 cifre. incearca din nou.")

#Ex 2
if len(numar) == 6:
    print("Acest numar are nici mai mult nici mai putin de sase cifre")
else:
    print("Nu avem 6 cifre in acest numar")

#Ex 3
if numar % 2 == 0:
    print("Numarul dumneavoastra nu este impar")
else:
    print("Numarul ales este impar.")

#Ex 4
numarX = input("Alege un numar X: ")
numarY = input("Alege inca un numar Y: ")
numarZ = input("Si al treilea Z: ")
if numarX > numarY and numarX > numarZ:
    print("Numarul X este cel mai mare !!")
elif numarZ > numarX and numarZ > numarY:
    print("Numarul Z este cel mai mare !!")
elif numarY > numarZ and numarY > numarX:
    print("Numarul Y este cel mai mare !!")
else:
    print("Nu ai un numar mai mare decat celelalte doua")

#Ex 5
unghi1 = int(input("Adauga primul unghi al triunghiului: "))
unghi2 = int(input("Adauga al doilea unghi al triunghiului: "))
unghi3 = int(input("Adauga al treilea unghi al triunghiului: "))

latura1 = input("Scrie lungimea primei laturi a triunghiului: ")
latura2 = input("Scrie lungimea laturei a doua a triunghiului: ")
latura3 = input("Scrie lungimea laturei a treia a triunghiului: ")

sumaUnghiuri = unghi3 + unghi1 + unghi2
if sumaUnghiuri == 180 and unghi1 > 0 and unghi2 > 0 and unghi3 > 0:
    print("Triunghiul este valid!")

#Ex 6
altapropozitie = 'Coral is either the stupidest animal or the smartest rock'
nrales = int(input("Alege un numar de la 1 la 20:"))
print(altapropozitie[0:-abs(nrales)])

#Ex 7
propnoua = str(altapropozitie[0:6]+altapropozitie[-6:])

#Ex 8
pozitie_rock = int(altapropozitie.find("rock"))
print(altapropozitie[0:pozitie_rock])

#Ex 9
string_nou = input("Creeaza un string aici: ").lower
assert string_nou[0] == string_nou[-1]
print("Caracterele sunt la fel.")

#Ex 10
string_doi = "0123456789"
nr_pare = string_doi[2::2]
nr_impare = string_doi[1::2]
print(nr_pare)
print(nr_impare)

#BONUS 1

varsta = int(input("Varsta ta este: ").strip())
print("Raspundeti cu DA sau NU la urmatoarele intrebari")
insotit_mama = str(input("Sunteti insotit de mama?: ").lower().strip())
insotit_tata = str(input("Sunteti insotit de tata?: ").lower().strip())
permisiune_mama = str(input("Aveti permisiune de la mama?: ").lower().strip())
permisiune_tata = str(input("Aveti permisiune de la tata?: ").lower().strip())
pasaport = str(input("Aveti pasaport?: ").lower().strip())

if varsta >= 18 and pasaport == "da":
    print("Aveti permisiunea de a va imbarca! ")
elif varsta >= 18 and pasaport == "nu":
    print("Nu aveti pasaport necesar pentru a va imbarca! ")
elif varsta < 18 and pasaport == "da" and insotit_mama == "da" and insotit_tata == "da":
    print("Aveti permisiunea de a va imbarca! ")
elif varsta < 18 and pasaport == "da" and insotit_mama == "nu" and insotit_tata == "da" and permisiune_mama == "da":
    print("Aveti permisiunea de a va imbarca datorita parintelui prezent si a permisiunii mamei! ")
elif varsta < 18 and pasaport == "da" and insotit_mama == "da" and insotit_tata == "nu" and permisiune_tata == "da":
    print("Aveti permisiunea de a va imbarca datorita parintelui prezent si a permisiunii tatlui! ")
elif varsta < 18 and pasaport == "nu" and insotit_tata == "da" and insotit_mama == "da":
    print("Este necesar pasaportul minorului pentru a va imbarca! ")
else:
    print("Nu aveti permisiunea sa ma imbarcati datoria lipsei unui parinte sau a permisiunii acestuia. ")

#BONUS 2

import random
zar_ales = int(input("Ghiceste zarul selectand  un numar de la 1 la 6: "))
zar_random = random.choice([1, 2, 3, 4, 5, 6])
print(zar_random)
if zar_ales == zar_random:
    print("Felicitari.Ati ghicit numarul. ")
elif zar_ales > zar_random:
    print("Ai pierdut.Ati selectat un numar mai mare decat cel al zarului")
else:
    print("Ai pierdut.Ati selectat un numar mai mic decat cel al zarului.")