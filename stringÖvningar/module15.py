#Gör en Fastighets-klass som inte kan instansieras. Den skall ha properties Bostadsyta, Taxeringsvärde, Lägg även till en abstrakt
# metod GetFastighetsavgift. Skapa sedan två subklasser som ärver från Fastighet: Villa med egenskapen TomtYta och Lägenhet med 
# egenskapen Lägenhetsnummer.

#Implementera metoden Fastighetsavgift i respektive subklass. För Villa skall Fastighetsavgift returnera 0,75 % av taxeringsvärdet,
#
# dock max 7112 kr. För Lägenhet skall Fastighetsavgift returnera 0,3 % av taxeringsvärdet, dock max 1217 kr.

#Skapa slutligen kod som instansierar en Villa och en Lägenhet. Skapa kod som sätter taxeringsvärde samt räknar ut fastighetsavgift
# för respektive fastighet.

#OBS: implementera med "bra" OOP-tänk: - beskrivningen ovan är generell utan hänsyn till programmeringsspråk. Att köra 
#engelska/svengelska begrepp går såklart bra!

from abc import ABC,abstractmethod

class Fastighet(ABC):
    def __init__(self,Bostadsyta):
        self._Bostadsyta=Bostadsyta
        self._Taxeringsvärde=0
    
    @abstractmethod
    def getFastighetsavgift(self):
        pass

class Villa(Fastighet):
    def __init__(self, TomtYta,Bostadsyta):
        super().__init__(Bostadsyta)
        self._TomtYta=TomtYta

    def setTaxeringsvärde(self,Taxeringsvärde):
        self._Taxeringsvärde=Taxeringsvärde

    def getFastighetsavgift(self):
        avgift=0.0075*self._Taxeringsvärde
        if avgift>7112:
            return 7112
        else:
            return avgift

class Lägenhet(Fastighet):
    def __init__(self, Lägenhetsnummer,Bostadsyta):
        super().__init__(Bostadsyta)
        self._Lägenhetsnummer=Lägenhetsnummer


    def setTaxeringsvärde(self,Taxeringsvärde):
        self._Taxeringsvärde=Taxeringsvärde

    def getFastighetsavgift(self):
        avgift=0.003*self._Taxeringsvärde
        if avgift>1217:
            return 1217
        else:
            return avgift

myVilla=Villa(400,200)
myApt=Lägenhet(112,65)
myVilla.setTaxeringsvärde(100000)
myApt.setTaxeringsvärde(700000)
print(myVilla.getFastighetsavgift())
print(myApt.getFastighetsavgift())
