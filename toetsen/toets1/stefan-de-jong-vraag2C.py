'''Programma voor vraag 2C'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

import random

rnd_getal = random.randint(1, 5)

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
    if rnd_getal == 1:
        print(f"Hallo, {voornaam} {achternaam} !")
    elif rnd_getal == 2:
        print(f"Hoi, {voornaam} {achternaam} !")
    elif rnd_getal == 3:
        print(f"Moi, {voornaam} {achternaam} !")
    elif rnd_getal == 4:
        print(f"Hai, {voornaam} {achternaam} !")
    elif rnd_getal == 5:
        print(f"Hey, {voornaam} {achternaam} !")

voornaamInput = input("Wat is je voornaam ? ")
achternaamInput = input("Wat is je achternaam ? ")
print_naam(voornaamInput, achternaamInput)