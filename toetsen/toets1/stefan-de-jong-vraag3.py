'''Programma voor vraag 3'''
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

def mk_array(cnt, rnd_min, rnd_max):
    """
    Return array met willekeurig aantal random getallen

    Parameters
    ----------
    cnt : int
        Variabele voor de aantal elementen in de lijst
    rnd_min : int
        Variabele voor de minimum waarde van de willekeurige getallen
    rnd_max : int
        Variabele voor de maximum waarde van de willekeurige getallen
    
    Return
    ----------
    gemaakteArray: array
        De array die gemaakt is wordt geretrouneerd
    """
    getal = 1
    gemaakteArray = [] * cnt

    while getal <= cnt:
        rnd_getal = random.randint(rnd_min, rnd_max)
        gemaakteArray.append(rnd_getal)
        getal += 1
    
    return gemaakteArray

def gem(getallen):
    """
    Return gemiddelde van alle getallen in de array

    Parameters
    ----------
    getallen : array
        De array met de getallen waar de gemiddelde van wordt berekend
    
    Return
    ----------
    gemiddelde : int
        Het gemiddelde wordt geretrouneerd
    """

    som = 0

    for getal in getallen:
        som += getal
    
    gem = som / len(getallen)
    gem = round(gem, 1)

    return gem
    
array = mk_array(15, 100, 1000)
index = 1

minimumGetal = float('inf')
maximumGetal = 0

for element in array:
    if index < 10:
        print(f"0{index}: {element}")
        index += 1
    else:
        print(f"{index}: {element}")
        index += 1
    
    if element < minimumGetal:
        minimumGetal = element
    elif element > maximumGetal:
        maximumGetal = element

print(f"Minimum getal is {minimumGetal}")
print(f"Maximum getal is {maximumGetal}")
print(f"Gemiddelde is {gem(array)}")