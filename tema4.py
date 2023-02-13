#Ex 1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for item in masini:
    print('Masina mrea preferata este ' + item +".")
print("------------------")

for i in range(len(masini)):
    print('Masina mrea preferata este ' + masini[i] +".")

print("------------------")
count = 0
while count < len(masini):
    print('Masina mrea preferata este ' + masini[count] +".")
    count += 1


print("--------------------------------------------")

#Ex 2
for i in range(1, len(masini) - 1):
    masini[i] = masini[i].upper()
else:
    print(masini)

print("--------------------------------------------")
#Ex 3
masini2 = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for item  in masini2:
    if item == "Mercedes":
        print("Am gasit masina " + item + "pt dvs !!!!!!!!!!")
    else:
        print("Am gasit masina " + item + ".Mai cautam." )

print("--------------------------------------------")
#Ex 4
for pretentie in masini2:
    if pretentie == "Lastun" or pretentie == "Trabant":
        continue
    else:
        print("S-ar putea sa va placa masina " + pretentie + "!")

print("--------------------------------------------")
#Ex 5
masini_vechi = []
for masinaaa1 in masini2:
    if masinaaa1 == 'Trabant' or masinaaa1 == 'Lastun':
        masini_vechi.append(masinaaa1)
        print(masini_vechi)
    else:
        continue

for i in range(len(masini2)):
    if masini2[i] == 'Lastun' or masini2[i] == 'Trabant':
        masini2[i] = 'Tesla'

print(masini2)

print("--------------------------------------------")
#Ex 6


pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
buget = 15000
for key, value in pret_masini.items():
    if value <= buget:
        print("Asta se incadreaza in bugetul dvs. si este masina: " + key)
    else:
        print("Aceasta depaseste bugetul dvs.")
    if value <= buget:
        print(key + " este masina potrivita si are pretul: " + str(value) )
    else:
        print("Aceasta depaseste bugetul dvs.")


print("--------------------------------------------")
#Ex 7
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
repetitii = 0
for numar in numere:
    if numar == 3:
        repetitii += 1
    else:
        continue
print("3 se repeta de " + str(repetitii) + " ori.")

print("--------------------------------------------")
#Ex 8

sumanumere = 0
for numar in numere:
    sumanumere += numar
print(sumanumere)

print("--------------------------------------------")
#Ex 9
biggest = 0
for numar in numere:
    if numar > biggest:
        biggest = numar
    else:
        continue
print(str(biggest) + " -> Este cel mai mare numar din lista.")

print("--------------------------------------------")
#Ex 10
for numar in range(0, len(numere)):
    if numere[numar] > 0:
        numere[numar] = numere[numar] * (-1)
    else:
        continue
print(numere)

