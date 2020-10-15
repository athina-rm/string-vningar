# Gör ett program där användaren får mata in en mening t ex ”Detta är min text
#som jag matar in”. Programmet skall räkna ut hur många ord meningen består av
#och meddela användaren om detta.

string=input("Enter the string: ")
print(f'You have entered {len(string.split(" "))} words')
