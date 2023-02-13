from abc import ABC, abstractmethod

class CarModel(ABC):
    @abstractmethod
    def volan(self):
        raise NotImplemented

    @abstractmethod
    def roti(self):
        raise NotImplemented

    @abstractmethod
    def scaune(self):
        raise NotImplemented

    def sistem_audio(self):
        print('Avem sistem audio')

class OldCar(CarModel):

    def __pilot_automat(self):                   #metoda privata
        print('Bunicul e pilotul automat')

    def _valoare_sentimentala(self):            #protected method
        self.__pilot_automat()
        print('Masina de colectie')


    def scaune(self):                             #metode publice
        print('4 scaune')

    def volan(self):
        print('Masina are volan pe stanga')

    def motor(self):
        print('Are motor diesel')

    def roti(self):
        print('Masina are roti de lemn')

class ModernCar(OldCar):

    def oglinzi(self):
        print('Are 5 oglinzi')

    def roti(self):
        print('Masina are roti de sticla')

    def absenabled(self):
        print('Are sistem abs')

    def airbag(self):
        print("Are 5 airbaguri")

    def extraoptiuni(self):
        self._valoare_sentimentala()


class BritishCar(ModernCar):
    def volan(self):
        print('Volan pe dreapta')

    def gps(self):
        print('Masina are gps')

class AlienCar(CarModel):

    def volan(self):
        print('Volan verde')

    def roti(self):
        print('Are si o roata de rezerva')

    def scaune(self):
        print('6 si din piele')


dacia = OldCar()
renault = ModernCar()
british_renault = BritishCar()


dacia.roti()
renault.roti()
british_renault.volan()
renault.volan()
alien = AlienCar()
alien.volan()
alien.roti()
renault._valoare_sentimentala()


# to do: creaza un pachet numit "car" si fiecare clasa sa fie mutata intr un fisier nou(clasa - modulul)
# crearea unui mini proiect folosind principiile oop care sa simuleze teste