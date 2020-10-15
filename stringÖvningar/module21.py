#Write a program that randomly names animal names!

#Create a function GetAnimalName (minChars, maxChars)

#the function should randomly display an animal name - of all the names in the list below that match the filter minChars and 
#maxChars.

#Ie GetAnimalName (7.9) - should give a random name of all names consisting of 7-9 letters

#PS: if there is no match at all then "" (empty string) must be returned

#(spaces are counted as a character!)

import random

def GetAnimalName(minChars, maxChars):
    lista= [   "MacGyver",

            "MacGonagall",

            "MacDonald",

            "Macahan",

            "MacThurbo",

            "Pascal",

            "Pilot",

            "PingPong",

            "Kristall",

            "Pucko",

            "Prinsessa",

            "Bubblan",

            "Fjollan",

            "Filur",

            "Baron von Münchausen",

            "Tiny Toledo",

            "Zelda",

            "Miss Maxina",

            "Zolita",

            "Oscar",

            "Leya",

            "Tequila",

            "Sunrise",

            "Bruce",

            "Lennart",

            "Greger",

            "Gunnar",

            "Gunnel",

            "Blåbär",

            "Billy",

            "Bob",

            "Sigbritt"

         ]
    newlist=[]
    for i in lista:
        if minChars<=len(i)<=maxChars:
            newlist.append(i)
    if len(newlist)==0:
        return ""
    animalName=random.choice(newlist)
    return animalName

print(GetAnimalName(7,9))