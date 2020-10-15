#Skapa en klass Organization som har egenskaperna Namn, Gatuadress, Ort, Webbadress. 

#Skapa ytterligare en klass Employee med egenskaperna Personnummer, Förnamn samt Efternamn. 

#Lägg sedan till ytterligare en egenskap (property) som du döper till Manager, i din Organization-klass, som är av typen Employee.

#Skapa slutligen kod som instansierar en ny Organization och en ny Employee och lägger till din person som Manager av din Organization

class Organization():
    def __init__(self,Name,Street, Place,Website):
        self._Name=Name
        self._Street=Street
        self._Place=Place
        self._Website=Website
        self._Manager:Employee

    def setManager(self,manager):
        self._Manager=manager

    def getManager(self):
        return self._Manager.getEmployeeDetails()

class Employee():
    def __init__(self,PersonNummer,Firstname,Surname):
        self._PersonNummer=PersonNummer
        self._Firstname=Firstname
        self._Surname=Surname

    def getEmployeeDetails(self):
        return self._Surname+" "+self._Firstname+ ":"+self._PersonNummer

myOrg1=Organization("Toppen AB","Gatustreet 13","Stockholm","toppen.com")
emp1=Employee("198002044536","Anna","Ohlsson")
myOrg1.setManager(emp1)
print(myOrg1.getManager())