#Skapa en klass Person. Den ska ha Name och BirthDate.

#Skriv ett program som ber användaren mata in antal personer.

#Mata in namn och birthdate  - personerna läggs  sen i en lista. 

#Skriv sedan ut hur många hela dagar gammal respektive person är (samt dess namn naturligtvis).

#Samt skriv ut hur många hela dagar gamla de är tillsammans.

#Programmet ska vara dynamiskt, det vill säga kör man programmet i morgon med exakt samma datum så ska alla personer vara en dag äldre.

#Klistra in all kod för klasserna samt koden som skapar instanserna i textrutan nedan.

#Exempel på hur programmet ska se ut när man kör det:

#Antal personer? 3
#Namn person 1: Stefan
#Födelsedag person 1: 1972-08-03
#Namn person 2: Josefine
#Födelsedag person 2: 2002-03-30
#Namn person 3: oliver
#Födelsedag person 3: 2008-05-28
#Stefan är 16988 antal dagar gammal.
#Josefine är 5743 antal dagar gammal.
#Oliver är 12952 antal dagar gammal.
#De är tillsammans 35683 dagar gamla.

from datetime import datetime,timedelta

class Person():
    def __init__(self,Name,Birthdate:datetime):
        self._Name=Name
        self._Birthdate=Birthdate

    def getName(self):
        return self._Name

    def getBirthday(self):
        return self._Birthdate

    def getAgeinDays(self):
        return (datetime.today()-self._Birthdate).days

count=int(input("Antal personer? "))
personsList=[]
for i in range(0,count):
    name=input(f"Namn person {i+1}: ")
    BirthdateString=input(f"Födelsedag person {i+1}(yyyy-mm-dd): ")
    Birthdate=datetime.strptime(BirthdateString,"%Y-%m-%d")
    personsList.append(Person(name,Birthdate))
sum=0
for i in personsList:
    print(f"{i.getName()} är {i.getAgeinDays()} antal dagar gammal.")
    sum+=i.getAgeinDays()
print(f"De är tillsammans {sum} dagar gamla.")