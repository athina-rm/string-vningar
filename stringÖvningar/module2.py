#2. Be användaren mata in 3 strängar. Skriv ut den sträng som är LÄNGST! Dessutom hur många tecken den är
Textlist=[]
for x in range (0,3):
    txt = input("mata in text :")
    Textlist.append(txt)
longeststring=""
for x in Textlist:
    if len(x)>len(longeststring):
        longeststring=x
print(f"The longest string is {longeststring}")
print(f"The length of the longest string is {len(longeststring)}")