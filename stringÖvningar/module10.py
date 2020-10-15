# Be användare mata in ett ord eller en mening. Programmet skall kontrollera om det
#ordet är en palindrom dvs om ordet blir likadant om man läser framifrån och bakifrån.
#Exempel på palindrom är namn som ”anna” eller ”otto” eller en mening som ”ni talar
#bra latin”. Meddela användaren om det är en palindrom eller ej.

string=input("Enter the string : ")
b=string.replace(" ", "")
for i in range (0,int(len(string)/2)):
    if b[i]==b[-(i+1)]:
        palindrome=True
    else:
        palindrome=False
        print("entered string is not a palindrome")
        break
if palindrome==True:
    print("entered string is a palindrome")

