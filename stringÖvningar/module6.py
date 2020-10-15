#6. Du har en sträng med texten ”Detta är en sträng som du skall ändra”. Ersätt via kod alla blanktecken i strängen
# med tecknet * . Räkna sedan ut via kod hur många förekomster det finns av tecknet * i strängen. 

s = "Detta är en sträng som du skall ändra"
s=s.replace(" ","*")
print(s.count("*"))

