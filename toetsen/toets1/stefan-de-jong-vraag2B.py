'''Programma voor vraag 2B'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

def print_naam(voornaam, achternaam):
    """
    Print voor en achternaam op het scherm

    Parameters
    ----------
    voornaam : string
        Variabele voor de voornaam van de gebruiker
    achternaam : int
        Variabele voor de achternaam van de gebruiker
    """
    print(f"Hallo, {voornaam} {achternaam} !")

voornaamInput = input("Wat is je voornaam ? ")
achternaamInput = input("Wat is je achternaam ? ")
print_naam(voornaamInput, achternaamInput)