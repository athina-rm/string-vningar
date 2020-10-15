#. Be användaren mata in en mailadress. Programmet skall kontrollera att inmatningen är rätt dvs att det finns 
#ett @ tecken och att det finns en . med 2 eller 3 tecken efter. Meddela användaren om det är rätt eller felaktig 
#adress
mailid=input("Mata in mailadress : ")
index=mailid.find("@")
if index!=-1 and (mailid[index+3]=="." or mailid[index+4]=="."):
    print ("adress är okej")
else:
    print ("felaktig adress")
