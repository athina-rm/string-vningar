#4. Du har en strängvariabel som ser ut så här string b ="I am a Python hacker." 
#a. Skriv ut vilken position sista a har 
#b. Skriv ut i vilken position ”P"  har i strängen ovan. Skriv samtidigt ut längden på hela strängen ovan
#c. Skriv ut varje ord för sig under varandra i en skärmutskrift 
#d. Plocka ut delsträngen ' hacker' ur b ovan via kod och skriv på skärmen 
#e. Gör om strängen b så att den ser ut så här:" i Am A C# hAcKeR" 

b ="I am a Python hacker." 
index=b.rfind("a")
print(f'sista "a" is there in position {index} ')
index=b.find("P")
print(f'"P" is there in position {index} ')
print(f"the length of the given string is {len(b)}")
b_wordlist=(b.split(" "))
for word in b_wordlist:
    print(word)
b=b.replace(" hacker","")
print(b)

