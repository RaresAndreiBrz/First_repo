class Cerc():
    import math
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Aceasta e culoarea: {self.culoare}')
        print(f'Aceasta e raza: {self.raza}')

    def arie(self, pi=3.14):
        return self.raza ** 2 * pi

    def diametrul_cerc(self):
        return self.raza * 2

    def circumferinta_cerc(self, pi=3.14):
        return 2 * float(self.raza) * pi


class Dreptunghi():
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie_dreptunghi(self):
        print(f'Aceasta este lungimea: {self.lungime}')
        print(f'Aceasta este latime: {self.latime}')
        print(f'Aceasta este culoare: {self.culoare}')

    def arie_dreptunghi(self):
        return self.lungime * self.latime

    def perimetrul_dreptunghi(self):
        return self.lungime * 2 + self.latime * 2

    def schimba_culoarea(self, new_culoare):
        self.culoare = new_culoare


class Angajat():
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie_angajat(self):
        print(f'Acest angajat se numeste {self.nume} {self.prenume} si are {self.salariu} salariu')

    def nume_complet(self):
        nume_complet = f'{self.nume} {self.prenume}'
        print(f'Angajatul se numeste {nume_complet} .')

    def salariu_lunar(self):
        salariu_lunar = self.salariu / 12
        print(f'Angajatul are salariu pe luna {salariu_lunar} .')

    def salariu_anual(self):
        return f'Angajatul are salariu pe an {self.salariu} .'

    def marire_salariu(self, marire):
        self.salariu = self.salariu + marire
        return f'Noul salariu al angajatului este {self.salariu} .'


cerc1 = Cerc("4", "rosu")
cerc1.descrie_cerc()
print(cerc1.descrie_cerc())
cerc1.diametrul_cerc()
print(cerc1.diametrul_cerc())
cerc1.circumferinta_cerc()
print(cerc1.circumferinta_cerc())

dreptunghi1 = Dreptunghi(10, 5, "verde")
dreptunghi1.descrie_dreptunghi()
print(dreptunghi1.descrie_dreptunghi())
dreptunghi1.arie_dreptunghi()
print(dreptunghi1.arie_dreptunghi())
dreptunghi1.perimetrul_dreptunghi()
print(dreptunghi1.perimetrul_dreptunghi())
dreptunghi1.schimba_culoarea("rosuuuu")
print(dreptunghi1.descrie_dreptunghi())

angajat1 = Angajat("Marian", 'Vanghelie', 222222)
angajat1.nume_complet()
angajat1.descrie_angajat()
print(angajat1.descrie_angajat())
angajat1.salariu_lunar()
print(angajat1.salariu_lunar())
print(angajat1.salariu_anual())
angajat1.marire_salariu(33)
print(angajat1.marire_salariu(0))


class Cont():
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularu {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self, cat_se_retrage):
        self.sold = self.sold - cat_se_retrage
        print(f'S-au retras {cat_se_retrage} si au ramas {self.sold} lei in cont')

    def creditare_cont(self, creditare_amount):
        self.sold = self.sold + creditare_amount
        print(f'S-au adaugat {creditare_amount} lei si acum sunt {self.sold} lei in cont')


class Factura():
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantit_noua):
        self.cantitate = cantit_noua
        print(f'Aceasta este cantitatea: {self.cantitate} kg')

    def schimba_pretul(self, valoare):
        self.pret_buc = valoare
        print(f'Acesta este pretul per bucata in lei {self.pret_buc}')

    def schimba_nume_produs(self, noul_nume):
        self.nume_produs = noul_nume
        print(f'Acesta este noul nume al produsului {self.nume_produs}.')

    def genereaza_factura(self):
        print(f'Factura cu seria S001, cu numarul {self.numar}')
        from datetime import date
        ziua = date.today()
        total = self.pret_buc * self.cantitate
        print(f'Data de azi:{ziua}')
        print(f'  Produs  | Cantitate| Pret_buc| Total')
        print(f'   {self.nume_produs} |    {self.cantitate}    |    {self.pret_buc}  |   {total}')


produs1 = Factura(1, 'cartofi', 888888, 999991)
print(produs1.schimba_cantitatea(20))
print(produs1.schimba_pretul(15))
print(produs1.schimba_nume_produs('pepeni'))
print(produs1.genereaza_factura())

class Masina:
    culoare = "gri"
    culori_disponibile = {"maro", "negru", "alb", "rosu ", "albastru"}
    marca = "Lancia"
    viteza_actuala = 0
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):

  print(f'Este o masina marca {self.marca}, de culoare {self.culoare}, inmatriculata {self.inmatriculata}, ce are ca viteza maxima {self.viteza_maxima} km/ora')

    def inmatriculare(self):
        self.inmatriculata = True
        print(f'Masina este inmatriculata. {self.inmatriculata}')

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
            print(f'Masina este acum de culoare {self.culoare}.')
        else:
            print("Culoarea nu este disponibila.")

    def accelereaza(self, viteza):
        if viteza > self.viteza_maxima:
            print(f"Nu se poate accelera mai mult de {self.viteza_maxima}")
            print(f'Ati atins viteza maxima de {self.viteza_maxima}.')
        elif viteza < self.viteza_maxima:
            self.viteza_actuala = viteza
            print(f"Viteza actuala este {self.viteza_actuala} km/ora.")
        else:
            print('Viteza nu exista')

    def franeaza(self):
        if self.viteza_actuala > 0:
            print("Ati franat. Viteza este 0 km/ora")
            self.viteza_actuala = 0
        else:
            print("Sunteti deja oprit")



masina1 = Masina('xa9129', 150)
print(masina1.descrie())
print(masina1.accelereaza(25))
print(masina1.franeaza())
print(masina1.vopseste('alb'))
masina1.inmatriculare()
print(masina1.inmatriculata)


class TodoList:
    taskurile = {}

    def adauga_task(self, nume, descriere):
        self.nume = nume
        self.descriere = descriere
        self.taskurile[self.nume] = [self.descriere]
        print(self.taskurile)

    def finalizeaza_task(self, nume):
        if nume in self.taskurile:
            del self.taskurile[nume]
            print(f'Astea sunt taskurile ramase: {self.taskurile}')
        else:
            print("Nu exita taskul asta")

    def afiseaza_todo_list(self):
        print(list(self.taskurile.keys()))

    def afiseaza_detalii_suplimentare(self, nume):
        if nume not in self.taskurile:
            a = str(input("Taskul nu e in lista. Doriti sa il adaugati? DA sau NU: ").lower())
            if a == "da":
                b = str(input("Ce descriere doriti la task?: ").lower())
                self.taskurile[nume] = [b]
                print(f'Taskul a fost adaugat. Uite l aici in lista: {self.taskurile}')
            else:
                print("Taskul nu a fost adaugat")
        else:
            print("Taskul e deja pe lista")

task1 = TodoList()
task1.adauga_task("pisica", "hraneste si spala")
task2 = TodoList()
task2.adauga_task("caine", "scoate l afara")
task1.finalizeaza_task("pisica")
TodoList.afiseaza_todo_list(task1)
task3 = TodoList()
task3.afiseaza_detalii_suplimentare("animal")