lista_jucatori_teren = ['Mara', 'Ion', 'Dobrin', 'Paul', 'Mirela']
lista_jucatori_rezerva = ['Marian', 'John', 'Alex', 'Ana', 'Laur']
print("In teren se afla: ")
print(lista_jucatori_teren)
print("Pe banca se afla: ")
print(lista_jucatori_rezerva)
lista_jucatori_scosi = []
schimbari_efectuate = 0
schimbari_max = 3
cine_intra = str(input("Alege numele jucatorului care intra: ")).capitalize()
cine_iese = str(input("Alege numele jucatorului care iese: ")).capitalize()
print("Iese jucatorul: "+cine_iese)
print("Intra jucatorul: "+cine_intra)

if cine_iese in lista_jucatori_teren and cine_intra in lista_jucatori_rezerva:
    lista_jucatori_teren.append(cine_intra)
    lista_jucatori_scosi.append(cine_iese)
    lista_jucatori_teren.remove(cine_iese)
    lista_jucatori_rezerva.remove(cine_intra)
    print(lista_jucatori_teren)
    print(lista_jucatori_rezerva)
    print(lista_jucatori_scosi)
    schimbari_efectuate = schimbari_efectuate + 1
    schimbari_max = schimbari_max - 1
    if schimbari_max == 2:
        print("Mai ai 2 schimbari posibile")
    elif schimbari_max == 1:
        print("Mai ai o schimbare posibile")
    else:
        print("Nu mai sunt schimbari disponibile")
else:
    print("Nu se poate efectua schimbarea deoarece jucatorul nu e in teren sau a fost deja schimbat’")

print("In teren se afla: ")
print(lista_jucatori_teren)
print("Pe banca se afla: ")
print(lista_jucatori_rezerva)

cine_intra = str(input("Alege numele jucatorului care intra: ")).capitalize()
cine_iese = str(input("Alege numele jucatorului care iese: ")).capitalize()
print("Iese jucatorul: "+cine_iese)
print("Intra jucatorul: "+cine_intra)

if cine_iese in lista_jucatori_teren:
    lista_jucatori_teren.append(cine_intra)
    lista_jucatori_scosi.append(cine_iese)
    lista_jucatori_teren.remove(cine_iese)
    lista_jucatori_rezerva.remove(cine_intra)
    print(lista_jucatori_teren)
    print(lista_jucatori_teren)
    print(lista_jucatori_scosi)
    schimbari_efectuate = schimbari_efectuate + 1
    schimbari_max = schimbari_max - 1
    if schimbari_max == 1:
        print("Mai ai o schimbare posibile")
    else:
        print("Nu mai sunt schimbari disponibile")
else:
    print("Nu se poate efectua schimbarea deoarece jucatorul nu e in teren sau a fost deja schimbat’")

print("In teren se afla: ")
print(lista_jucatori_teren)
print("Pe banca se afla: ")
print(lista_jucatori_rezerva)

cine_intra = str(input("Alege numele jucatorului care intra: ")).capitalize()
cine_iese = str(input("Alege numele jucatorului care iese: ")).capitalize()
print("Iese jucatorul: "+cine_iese)
print("Intra jucatorul: "+cine_intra)

if cine_iese in lista_jucatori_teren:
    lista_jucatori_teren.append(cine_intra)
    lista_jucatori_scosi.append(cine_iese)
    lista_jucatori_teren.remove(cine_iese)
    lista_jucatori_rezerva.remove(cine_intra)
    print(lista_jucatori_teren)
    print(lista_jucatori_teren)
    print(lista_jucatori_scosi)
    schimbari_efectuate = schimbari_efectuate + 1
    schimbari_max = schimbari_max - 1
    if schimbari_max == 1:
        print("Mai ai o schimbare posibile")
    else:
        print("Nu mai sunt schimbari disponibile")
else:
    print("Nu se poate efectua schimbarea deoarece jucatorul nu e in teren sau a fost deja schimbat’")