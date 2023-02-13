# Exercitiul 1

# variabila este ca un sertar din memorie , unde este depozitata informatie (caractere, numere, etc)

# Exercitiul 2
nume = "Rares"
varsta = 26
greutate_kg = 71.6
amator = True

# Exercitiul 3
print(type(nume))

# Exercitiul 4
greutate_kg = round(greutate_kg)
print(greutate_kg)
print(type(greutate_kg))

# Exercitiul 5
print(f"{nume} este numele concurentului.")
print(f"Varsta concurentului este: {varsta} ani.")
print(f"Greutatea inainte de concurs: {greutate_kg} kg.")
print(f"Concurentul este un sportiv amator: {amator} ." )

# Exercitiul 6
nume = input("Numele de familie este: ")
prenume = input("Prenumele tau este: ")
nrCaractere = int(len(nume)) + int(len(prenume))
print(f"Numele complet al sportivului are " + str(nrCaractere) + " caractere.")

# Exercitiul 7
lungime = 10
latime = 3
aria = lungime * latime
print(f"Aria dreptunghiului este: " + str(aria) + ".")

# Exercitiul 8
propozitia = "Coral is either the stupidest animal or the smartest rock"
propozitia.count("the")

# Exercitiul 9
propozitia = "Coral is either the stupidest animal or the smartest rock"
result = propozitia.count("the")
print(result)

# Exercitiul 10

propozitia = "Coral is either the stupidest animal or the smartest rock"

assert propozitia.isdigit() == False
print(" nu este format doar din numere")

# Exercitiul 1 next level
pisici = "12345"
pisici_lenght = len(pisici)
mid_index = pisici_lenght // 2
print(pisici[mid_index])

if len(pisici) % 2 == 1:
  print('Stringul are o dimensiune impară')
else:
  print('Stringul are o dimensiune pară')

# Exercitiul 2
bautura = "apa"
invers_bautura = bautura[::-1]
assert bautura == invers_bautura

# Exercitiul 3
alaba, porto = "alabala", "portocala"
print(alaba)
print(porto)

# Exercitiul 4
a , b = alaba[0], porto[0]
# !!!! nu reusesc partea cu capitalizarea

# Exercitiul 5
user = input("Alegeti un username: ")
password = input("Alegeti o parola: ")
passhidden = len(password) * "*"
print("Parola pt userul " + user + " este " + passhidden + " si are " + str(len(password)) + " caractere." )