'''Programma voor drie lijnen'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4]

y1 = [0, 1, 2, 3]
y2 = [1, 2, 3, 4]
y3 = [2, 3, 4, 5]

plt.plot(x_values, y1, 'b--o', label="Lijn 1")
plt.plot(x_values, y2, 'r:d', label="Lijn 2")
plt.plot(x_values, y3, 'g-.x', label="Lijn 3")

plt.xlabel("x-as")
plt.ylabel("y-as")
plt.title("Mijn Grafiek")

plt.legend()

plt.show()
