'''Programma voor lijngrafiek tweedegraadsfunctie'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

import numpy as np
import matplotlib.pyplot as plt

def bereken_discriminant(a, b, c):
    return b**2 - 4*a*c

def bereken_nulpunten(a, b, c, D):
    if D > 0:
        x1 = (-b + np.sqrt(D)) / (2*a)
        x2 = (-b - np.sqrt(D)) / (2*a)
        return x1, x2
    elif D == 0:
        x = -b / (2*a)
        return x,
    else:
        return None

def bereken_top(a, b, c):
    x_top = -b / (2*a)
    y_top = a*x_top**2 + b*x_top + c
    return x_top, y_top

a = float(input("Voer waarde voor a in: "))
b = float(input("Voer waarde voor b in: "))
c = float(input("Voer waarde voor c in: "))
x_start = float(input("Voer startwaarde voor x-as in: "))
x_eind = float(input("Voer eindwaarde voor x-as in: "))

D = bereken_discriminant(a, b, c)
nulpunten = bereken_nulpunten(a, b, c, D)
x_top, y_top = bereken_top(a, b, c)

x = np.linspace(x_start, x_eind, 500)
y = a*x**2 + b*x + c

plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f"y = {a}x² + {b}x + {c}", color="blue")
plt.title(f"Tweedegraadsfunctie: y = {a}x² + {b}x + {c}", fontsize=14)
plt.xlabel("x-as", fontsize=12)
plt.ylabel("y-as", fontsize=12)

if nulpunten:
    for i, nulpunt in enumerate(nulpunten, start=1):
        plt.scatter(nulpunt, 0, color="red")
        plt.text(nulpunt, 1, f"Nulpunt{i}=({nulpunt:.1f}, 0)", fontsize=10)

plt.scatter(x_top, y_top, color="green")
plt.text(x_top, y_top + 1, f"Top=({x_top:.1f}, {y_top:.1f})", fontsize=10)

plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(f"fig-{a}x²+{b}x+{c}.png")
plt.show()
