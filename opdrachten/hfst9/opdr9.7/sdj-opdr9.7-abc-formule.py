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

import math

# Maak functie aantal_nulpunten(a, b, c) aan

def aantal_nulpunten(a, b, c):
    d = (pow(b, 2) - 4 * a * c)

    if d > 0:
        nulpunten = 2
    elif d == 0:
        nulpunten = 1
    elif d < 0:
        nulpunten = 0
    
    return nulpunten

# Maak functie abc_formule(a, b, c) aan

def abc_formule(a, b, c):
    resultaat1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / 2 * a
    resultaat2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / 2 * a

    return resultaat1, resultaat2

# Maak functie parabool_xtop(a, b, c) en parabool_ytop(a, b, c, x) aan

def parabool_xtop(a, b, c):
    x_top = -b / (2 * a)

    return x_top

def parabool_ytop(a, b, c, x):
    y_top = (a * math.pow(x, 2)) + (b * x) + c

    return y_top

# Maak functie parabool_type(a, b, c, x) aan

def parabool_type(a, b, c, x):
    A = a * math.pow(x, 2) + b * x + c

    if A > 0:
        type = "bergparabool"
    elif A < 0:
        type = "dalparabool"

    return type

print("Gegeven de volgende tweedegraadsfunctie")
print("y = ax² + bx + c")
print("")

print("Geef a?")
a = int(input(""))

print("Geef b?")
b = int(input(""))

print("Geef c?")
c = int(input(""))

x = parabool_xtop(a, b, c)

nulx1, nulx2 = abc_formule(a, b, c)

print("De tweedegraads functie is: y =", str(a) + "x² +", str(b) + "x + ", str(c))
print("De functie is een", parabool_type(a, b, c, x), "op x,y positie (", str(x), ", ", parabool_ytop(a, b, c, x), ")")
print("De tweedegraadsfunctie heeft", aantal_nulpunten(a, b, c), "nulpunt(en)")
print(f"De x-waarden voor de nulpunten zijn ({nulx2}, {nulx1})" )