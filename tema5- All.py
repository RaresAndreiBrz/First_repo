print("---------------------Exercitiul 1---------------------------")
#Exercitiul 1

def calculeazasuma():
    nr1 = int(input("Alege un numar: "))
    nr2 = int(input("Alege un numar: "))
    suma = nr1 + nr2
    return suma


print(calculeazasuma())

print("------------------Exercitiul 2-------------------------")
#Exercitiul 2

def parimpar():
    nr3 = int(input("Alege un numar: "))
    if nr3 % 2 == 0:
        print(True)
    else:
        print(False)



print(parimpar())

print("-----------------Exercitiul 3----------------------------")
#Exercitiul 3

def lungimenume():
    nume = input("Numele tau de familie este: ")
    prenume = input("Preumele tau este: ")
    return len(nume + prenume)


print(lungimenume())


print("--------------------Exercitiul 4----------------------")
#Exercitiul 4

def ariadreptunghi():
    lungimedrept = int(input("Lungimea dreptunghiului este : "))
    latimedrept = int(input("Latimea dreptunghiului este : "))
    return lungimedrept * latimedrept


print(ariadreptunghi())


print("--------------------Exercitiul 5----------------------")
#Exercitiul 5

import math as M
def ariecerc():
    raza = float(input("Care este raza cercului? : "))
    aria = M.pi * raza**2
    return aria


print(ariecerc())


print("--------------------Exercitiul 6----------------------")
#Exercitiul 6

def existasaunu():
    string = input("uimeste-ma cu un string te rog: ")
    character = str(input("Ce caracter cauti?: "))
    if character in string:
        return True
    else:
        return False


print(existasaunu())

print("--------------------Exercitiul 7----------------------")
#Exercitiul 7

def lowerupper(propozitie):
    charmici = 0
    charmari = 0
    for x in propozitie:
        if x.islower():
            charmici += 1
        elif x.isupper():
            charmari += 1
        else:
            pass
    print("Nr de caractere lower case este :" + str(charmici))
    print("Nr de caractere upper case este :" +str(charmari))


print(lowerupper("abcd BBBB 2"))


print("--------------------Exercitiul 8----------------------")
#Exercitiul 8

def nrpozitive(list):
    return [numar for numar in list if numar > 0]


print(nrpozitive([ 2, 323, 0, -2, -5]))


print("--------------------Exercitiul 9----------------------")
#Exercitiul 9

def bigger(a,b):
    if a > b:
        print("Numarul" + a + "este mai mare decat " + b + ".")
    elif a < b:
        print("Numarul" + a + "este mai mic decat " + b + ".")
    else:
        print("Numarul" + a + "este egal cu " + b + ".")

print(bigger(1,2))

print("--------------------Exercitiul 10----------------------")
#Exercitiul 10

def addinset(numar, set):
    if numar in set:
        print("Exista numarul deja in acest set.")
        return False
    elif numar not in set:
        set.add(numar)
        print("Am adaugat numarul in set")
        return True
    else:
        print("Ceva nu e bine")


print(addinset(17, {1,2,3,4,5}))


print("---OPTIONAL--------Exercitiul 1----------------------")
#Exercitiul 1

def zilelelunii(luna):
    luni = {"ianuarie": 31, "februarie": 28, "martie": 31, "aprilie": 30, "mai": 31, "iunie": 30, "iulie": 31, "august": 31,
            "septembrie": 30, "octombrie": 31, "noiembrie": 30, "decembrie": 31}
    zilelelunii = luni.get(luna)
    if luna in luni:
        return f"{luna} are {zilelelunii} zile."
    else:
        return "Luna introdusa este incorecta."


print(zilelelunii("ianuarie"))


print("---OPTIONAL--------Exercitiul 2----------------------")
#Exercitiul 2

def matematica(x, z):
    return x + z, x - z, x * z, x / z
    a = x + z
    b = x - z
    c = x * z
    d = x / z
    print(a)
    print(b)
    print(c)
    print(d)


print(matematica(4,2))

print("---OPTIONAL--------Exercitiul 3----------------------")
#Exercitiul 3

from collections import Counter
def countinginlist(list):
    numeremici = [numar for numar in list if 0 <= numar < 10]
    return dict(Counter(numeremici))

baza = [1,3,41,14,12,1,2,4,5,123,123,123,123,123]

print(countinginlist(baza))


print("---OPTIONAL--------Exercitiul 4----------------------")
#Exercitiul 4

def biggest(a, b, c):
    return max(a, b, c)
print(biggest(1,32224,1232))

print("---OPTIONAL--------Exercitiul 5----------------------")
#Exercitiul 5

def calculeazatot(a):
    b = 0
    for i in range(0, a):
        b += i + 1

    return b


print(calculeazatot(5))

print("---OPTIONAL--------Exercitiul 6----------------------")
#Exercitiul 6

def nrcomune(list1, list2):
    a = []
    for i in list1:
        if i in list2:
            a.append(i)

    print(a)

list1 = [1, 1, 2, 7, 3]

list2 = [2, 2, 3, 7, 4]

print(nrcomune(list1, list2))

print("---OPTIONAL--------Exercitiul 7----------------------")
#Exercitiul 7


def reducere(pret):
    reducerea = float(pret - pret/10)
    if reducerea > 0:
        print("Pretul final este acesta: " + str(reducerea) + "lei.")
    else:
        print("Pretul este incorect!")


print(reducere(120.5))

print("---OPTIONAL--------Exercitiul 8----------------------")
#Exercitiul 8

import datetime

def datasioraacum():
    romania = datetime.datetime.now() + datetime.timedelta(hours=0)
    china = datetime.datetime.now() + datetime.timedelta(hours=6)
    print(f'Acum in Romania: {romania.strftime("%Y-%m-%d %H:%M:%S")}')
    print(f'Acum in China: {china.strftime("%Y-%m-%d %H:%M:%S")}')

print(datasioraacum())

print("---OPTIONAL--------Exercitiul 9----------------------")
#Exercitiul 9

def zilepanalaziuata(data):
    azi = datetime.datetime.today()
    data = datetime.datetime.strptime(data, '%y-%m-%d')
    zileramase = data - azi
    return zileramase.days

print(zilepanalaziuata(1996/04/28))