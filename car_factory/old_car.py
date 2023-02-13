class OldCar(CarModel):

    def __pilot_automat(self):                   #metoda privata
        print('Bunicul e pilotul automat')

    def _valoare_sentimentala(self):            #protected method
        self.__pilot_automat()
        print('Masina de colectie')


    def scaune(self):                            #metode publice
        print('4 scaune')

    def volan(self):
        print('Masina are volan pe stanga')

    def motor(self):
        print('Are motor diesel')

    def roti(self):
        print('Masina are roti de lemn')