#Skriv en funktion som räknar ut totala antalet bokstäver i en lista som den ovan. Dvs summan av längden av alla element

def characterCount(list):
    count=0
    for i in list:
        count+=len(i)
    return count


cities = [ "Stockholm", "Göteborg", "Malmö", "Köpenhamn", "London" ]
print(characterCount(cities))