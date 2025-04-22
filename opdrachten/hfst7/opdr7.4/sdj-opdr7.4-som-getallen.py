'''Programma voor som der getallen'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

import math

# Maak variabelen aan

getal = 250
totaalGetal = 0

getallen = []

# Loop totdat getal 500 is en print som etc.

while getal <= 500:
    totaalGetal += getal
    kwadraat = math.pow(getal, 2)
    getallen.append(getal)

    print("Getal " + str(getal) + "      Som " + str(totaalGetal) + "      Kwadraat " + str(kwadraat))

    getal += 1
else:
    lengte = len(getallen) 
    som = sum(getallen)

    gemiddelde = som / lengte
    print("Het gemiddelde van alle getallen is: " + str(gemiddelde))