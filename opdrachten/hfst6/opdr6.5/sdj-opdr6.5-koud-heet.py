'''Programma voor koud of heet'''
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

print("Geef de temperatuur in °C")
getalStr = input("")

getalInt = int(getalStr)

# Check of getal koud of heet is en print resultaat

if getalInt < 0: 
    print("Het is koud!")
elif getalInt >= 0 and getalInt <= 10:
    print("Het is fris!")
elif getalInt >= 11 and getalInt <= 17:
    print("Het is koel!")
elif getalInt >= 18 and getalInt <= 24:
    print("Het is lekker weer!")
elif getalInt >= 25 and getalInt <= 31:
    print("Het is warm!")
elif getalInt >= 32 and getalInt <= 40:
    print("Het is erg warm!")
elif getalInt > 40:
    print("Het is heet!")