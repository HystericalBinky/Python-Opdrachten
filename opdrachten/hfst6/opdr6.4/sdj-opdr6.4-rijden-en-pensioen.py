'''Programma voor rijden en pensioen'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Vraag om getal en bewaar die in variabele

print("Wat is uw leeftijd?")
getalStr = input("")

getalInt = int(getalStr)

# Check of getal hoog genoeg is voor auto rijden en/of pensioen is en print resultaat

if getalInt < 0 or getalInt > 120: 
    print("Geef een geldige leeftijd op!")
elif getalInt < 18:
    print("Uw leeftijd is", getalInt)
    print("Je mag nog niet autorijden!")
elif getalInt >= 68:
    print("Uw leeftijd is", getalInt)
    print("Je mag met pensioen!")
elif getalInt > 18 and getalInt < 68:
    print("Uw leeftijd is", getalInt)
    print("Je mag autorijden maar nog niet met pensioen!")
