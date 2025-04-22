'''Programma voor vraag 4'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

import os, random, string

def maak_wachtwoord(aantal_karakters):
    """
    Return array met willekeurig aantal random getallen

    Parameters
    ----------
    aantal_karakters : int
        Variabele voor het aantal karakters in het wachtwoord
    
    Return
    ----------
    wachtwoord: string
        De wachtwoord die gemaakt is wordt geretrouneerd
    """
    if aantal_karakters < 8:
        aantal_karakters = 8

    chars = string.ascii_letters + string.digits + '!@#$%^&*()_+-=[]{}'
    random.seed = (os.urandom(1024))

    wachtwoord = ''.join(random.choice(chars) for i in range(aantal_karakters))
    return wachtwoord

print(f"{maak_wachtwoord(10)}")
print(f"{maak_wachtwoord(32)}")
print(f"{maak_wachtwoord(100)}")