'''Programma voor vraag naam'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak functie vraag_naam() aan

def vraag_naam():
    # Vraag om naam en bewaar die in variabele

    print("Wat is uw naam?")
    naam = input("")

    return naam

print("Hallo", vraag_naam())

print("")

print("Hallo", vraag_naam())