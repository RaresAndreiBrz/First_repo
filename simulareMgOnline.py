"""
input nume nastere cnp
verif user major, daca da se logh, daca nu il trimitem acasa
daca e major 0 incercam sa extragem din cnp anul nasterii si sa verif daca corespunde cu anul nasterii introdus
daca nu e ok - userul nu este lasat sa intre pe site
daca da extragem pe baza primei cifre din cnp daca userul e M sau F
daca e femeie se afiseaza un string cu parfum
daca e barbat un string cu pantofi
daca nu e nici M nici F - afiseaza "esti robot"
"""
data nasterii = input("Data nasterii zz/ll/aaaa: " +