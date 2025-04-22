'''Programma voor gokspelletje'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Importeren van een library om willekeurige getallen aan te maken
import random

# Maak variabelen aan

getal = ""

# Geeft een willekeurig getal tussen 1 en de 10
rnd_getal = random.randint(1, 10)

print("--- Gokspelletje ---")

print("")

while True:
    # Vraag om getal en bewaar die in variabele

    print("Geef een getal tussen de 1 en de 10")
    getal = input("")

    print("")

    # Check of getal goed of fout is en print resultaat

    if int(getal) == rnd_getal:
        print("Gefeliciteerd!")
        print("Getal", int(getal), "is goed!")
        print("")
        print("--------------------")
        print("")
        print("Tot ziens!")
        break
    elif int(getal) < rnd_getal:
        print("Jammer, getal", int(getal), "is the laag")
        print("")
        print("--------------------")
        print("")
    elif int(getal) > rnd_getal:
        print("Jammer, getal", int(getal), "is the hoog")
        print("")
        print("--------------------")
        print("")