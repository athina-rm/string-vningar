#Skriv ett program som matar in en text. För att förenkla kan vi säga att den ENDA separatorn mellan olika ord är mellanslag.

#Efter detta ska du  ta fram det längsta och det kortaste ordet och skriva ut. OBS: inte genom att använda inbyggda sorterings-rutiner 
#utan genom en for-loop och gå igenom alla  värden

text=input("Enter the text: ")
stringList=text.split()
longest=""
shortest=stringList[0]
for i in stringList:
    if len(i)<len(shortest):
        shortest=i
    elif len(i)>len(longest):
        longest=i
print (f"Longest word entered is {longest}")
print (f"Shortest word entered is {shortest}")

