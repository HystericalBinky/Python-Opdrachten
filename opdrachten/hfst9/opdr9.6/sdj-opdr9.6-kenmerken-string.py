'''Programma voor kenmerken string'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak functie kenmerken_string(str) aan

def kenmerken_string(str):
    aantal_karakters = len(str)
    aantal_woorden = len(str.split())

    woorden = str.split()
    gemmideld_karakters = sum(len(woord) for woord in woorden) / len(woorden)

    print("String is:", str)
    print("Aantal karakters is:", aantal_karakters)
    print("Aantal woorden is:", aantal_woorden)
    print("Gemiddeld aantal karakters per woord is:", gemmideld_karakters)

kenmerken_string(str = "Never lose a holy curiosity")
