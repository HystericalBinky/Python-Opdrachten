'''Programma voor subplotting, lijn- en scattergrafiek'''
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

plt.style.use('fivethirtyeight')

maanden_line = np.arange(1, 13, 1)
data_line = np.array([5, 8, 15, 10, 25, 30, 17, 19, 28, 20, 23, 26])

uren_scatter = np.arange(1, 7, 1)
data_scatter = np.array([9, 16, 12, 25, 17, 20])

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].plot(maanden_line, data_line, color='green', marker='o', label="Lijn")
axs[0].set_title("Groene lijngrafiek", fontsize=14)
axs[0].set_xlabel("maanden", fontsize=12)
axs[0].set_ylabel("euro's", fontsize=12)

axs[1].scatter(uren_scatter, data_scatter, color='red', label="Punten")
axs[1].set_title("Rode scattergrafiek", fontsize=14)
axs[1].set_xlabel("uren", fontsize=12)
axs[1].set_ylabel("euro's", fontsize=12)

plt.tight_layout()

plt.show()
