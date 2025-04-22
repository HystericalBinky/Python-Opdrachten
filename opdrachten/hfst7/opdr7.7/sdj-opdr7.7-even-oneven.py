'''Programma voor even en oneven'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak variabele getallen aan

getallen = '12,3,7,25,771,45,6,98,55,546'
getal = ''

# Loop door karakters

for karakter in getallen:
    if karakter == ',':
        if int(getal) % 2 == 0:
            print(str(getal) + " is even.")
        else:
            print(str(getal) + " is oneven.")

        getal = ''
    else:
        getal = getal + karakter
else:
    if int(getal) % 2 == 0:
        print(str(getal) + " is even.")
    else:
        print(str(getal) + " is oneven.")

    getal = ''