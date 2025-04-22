'''Programma voor eerste grafiek'''
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
import random

y_values = [random.randint(1, 10) for _ in range(5)]

x_values = [1, 2, 3, 4, 5]

plt.plot(x_values, y_values, marker='o')

plt.xlabel("x-as")
plt.ylabel("y-as")
plt.title("Willekeurige waarden")

plt.show()
