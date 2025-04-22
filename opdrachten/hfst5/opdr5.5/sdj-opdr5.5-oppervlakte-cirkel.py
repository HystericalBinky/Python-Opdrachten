'''Programma voor oppervlakte cirkel'''
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

print("Bereken de oppervlakte en de omtrek van een cirkel")
print("Geef de lengte van de straal van een cirkel (cm) ?")
straalStr = input("")

# Bereken oppervlakte en omtrek in variabele

pi = 3.141592653589793

straalInt = int(straalStr)
oppervlakteInt = round(straalInt * straalInt * pi, 1)
omtrekInt = round(2 * straalInt * pi, 1)

oppervlakteStr = str(oppervlakteInt)
omtrekStr = str(omtrekInt)

# Print resultaat op scherm.

print("De straal van de cirkel is " + straalStr + " cm")
print("De oppervlakte van de cirkel is " + oppervlakteStr + " cm²")
print("De omtrek van de cirkle is " + omtrekStr + " cm")