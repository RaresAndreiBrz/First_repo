print("--------------------------------------------")
#Ex 1 -OPTIONAL

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for altnumar in alte_numere:
    if altnumar >= 0 and altnumar % 2 == 0:
        numere_pare.append(altnumar)
        numere_pozitive.append(altnumar)
    elif altnumar >= 0 and altnumar % 2 != 0:
        numere_impare.append(altnumar)
        numere_pozitive.append(altnumar)
    elif altnumar < 0 and altnumar % 2 == 0:
        numere_pare.append(altnumar)
        numere_negative.append(altnumar)
    elif altnumar < 0 and altnumar % 2 != 0:
        numere_impare.append(altnumar)
        numere_negative.append(altnumar)
    else:
        print("Acesta nu e numar din cate imi dau seama.")
print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

print("--------------------------------------------")
#Ex 2 -OPTIONAL
for nr in range(len(alte_numere)):
    for nr2 in range(nr + 1, len(alte_numere)):
         if alte_numere[nr] > alte_numere[nr2]:
            alte_numere[nr], alte_numere[nr2] = alte_numere[nr2], alte_numere[nr]

print(alte_numere)

print("--------------------------------------------")
#Ex 3 -OPTIONAL
import random
numar_secret = random.randint(1, 30)
numar_ghicit = input("Alege un numar de la 0 la 30: ")
while (numar_ghicit != numar_secret):
    numar_ghicit = int(input("Go again: "))
    if numar_secret > numar_ghicit:
        print("Nr secret e mai mare")

    elif numar_secret < numar_ghicit:
        print('Its lower than that! Guess again!')
print('Felicitari. Ai terminat!.')

print("--------------------------------------------")
#Ex 4 -OPTIONAL
x = int(input("Alege un numar intre 1 si 10: "))
for i in range(0,x+1):
    print(i * str(i))

print("--------------------------------------------")
#Ex 5 -OPTIONAL
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
for numar1 in tastatura_telefon:
    for numar2 in range(len(numar1)):
        for numar2 in numar1:
            print(f'Cifra curenta este: {numar2}')
        break