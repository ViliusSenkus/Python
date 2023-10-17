#Klasės sukūrimas
class Klase:
            #Konstruktorius
      """
            #Konstruktorius pagal nutylėjimą

      def __init__(self):
            pass
            
            #įprastas konstruktorius

      def __init__(self, laukas1, laukas2):
            self.laukas1 = param1
            self.laukas2 = param2

      """

            #Laukai:
      laukas1 = None
      laukas2 = True
      
            #Funkcijos - Metodai
      def set_data(self, param1, param2):  #parametras 'self' leidžia pasiekti laukus
            self.laukas1 = param1
            self.laukas2 = param2
      
      def get_data(self):
            print("laukas1", self.laukas1, "laukas2", self.laukas2)

#Objketo sukūrimas
klase1 = Klase()

#Klasės laukų pasiekimas:
klase1.laukas1 = 'something'

#Klasės metodų naudojimas:
klase1.set_data('more_smth', False)
klase1.get_data()


class Klase2:
      k1 = None
      k2 = None

      def __init__(self, k1, k2):
            self.k1=k1
            self.k2=k2
            print("klasė sukurta, su parametrais", self.k1, self.k2)
      
     

klase2 = Klase2('pirmas','antras')


#Paveldėjimas
class Vaikas1(Klase):
      pass

class Vaikas2(Klase2):  #Galima paveldėti tik vieną klasę

      def __init__(self, k1, k2, v1):
            super(Vaikas2, self).__init__(k1,k2)
            self.v1 = v1

vaikas2=Vaikas2(1,2,3)

#Polimorfizmas
class Vaikas3(Klase):
      """
      Klasėje Klase turimas metodas:

      def get_data(self):
            print("laukas1", self.laukas1, "laukas2", self.laukas2)
      """

      def get_data(self):
            print("pridedama info ir tevines klases reiksmes", end = " ")
            super().get_data()
            

vaikas3=Vaikas3()
vaikas3.get_data()

#Inkapsuliacija
#Inkapsuliacija realizuota labai silpnai:
class Nauja:
      __vardas = 'vardas'

      # tokiu pat būsu kintamąjį __pavadinimas įdėjus į konstruktorių, jis pasiekiamas tik toje klasėje.

      def get(self):
            return self.__vardas

nauja1 = Nauja()
#print(nauja1.vardas)    --- nepasiekiama
nauja1.__vardas = 'dududud'
Nauja.__vardas = 'dar kazkoks' 
print(nauja1.__vardas)  
print(nauja1.get())
print(Nauja.__vardas)

#Dekoratoriai