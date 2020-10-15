#Write a program that right-aligns entered text. This is done by adding as many spaces at the beginning so that the line is 40 characters long. 
#Then the result is printed. If the entered string is empty or longer than 40 characters, the program ends.

#Otherwise you have to enter a new text which you must adjust to the right

#Paste the code in the box below
while True:
    string=input("Enter the text:")
    rightjustifiedString=""
    if 0<len(string)<=40:
        for i in range (0,41-len(string)):
            rightjustifiedString+=" "
        rightjustifiedString+=string
        print (rightjustifiedString)
    else:
        break
