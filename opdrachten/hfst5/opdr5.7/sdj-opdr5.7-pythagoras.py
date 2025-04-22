'''Programma voor pythagoras'''
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

# Vraag om getallen en bewaar die in variabelen

print("Geef de lengte van zijde 1")
zijde1Str = input("")
print("Geef de lengte van zijde 2")
zijde2Str = input("")

zijde1Float = float(zijde1Str)
zijde2Float = float(zijde2Str)

# Bereken lange zijde in variabele

langeZijdeKwadraat = zijde1Float**2 + zijde2Float**2
langeZijde = math.sqrt(langeZijdeKwadraat)

# Print resultaat op scherm.

print("")
print("Korte zijde 1 =", zijde1Float)
print("Korte zijde 2 =", zijde2Float)
print("Lange zijde   =", langeZijde)