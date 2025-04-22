'''Programma voor grafieken CBS-cijfers bevolking'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

file_path = 'opdrachten/hfst16/opdr16.12/bevolking-nl.csv'
data = pd.read_csv(file_path, sep=';', encoding='utf-8')

data = data.dropna(subset=['Perioden', 'TotaleBevolking_1', 'LevendGeborenKind_69', 'Overledenen_70', 'Ongehuwd_5', 'Gehuwd_6', 'Gescheiden_8'])

style.use('ggplot')

plt.figure(figsize=(12, 8))
plt.subplot(2, 3, 1)
plt.plot(data['Perioden'], data['TotaleBevolking_1'], 'm--')
plt.title('Bevolking Nederland 1950-2019')
plt.xlabel('Jaar')
plt.ylabel('Bevolking')

subset_1950_1960 = data[(data['Perioden'] >= 1950) & (data['Perioden'] <= 1960)]
plt.subplot(2, 3, 2)
plt.plot(subset_1950_1960['Perioden'], subset_1950_1960['TotaleBevolking_1'], 'm:')
plt.title('Bevolking 1950-1960')
plt.xlabel('Jaar')
plt.ylabel('Bevolking')

plt.subplot(2, 3, 3)
plt.plot(data['Perioden'], data['LevendGeborenKind_69'], label='Geboren', color='green')
plt.plot(data['Perioden'], data['Overledenen_70'], label='Overleden', color='red')
plt.title('Aantal overledenen & geboren')
plt.xlabel('Jaar')
plt.ylabel('Aantal')
plt.legend()

plt.subplot(2, 3, 4)
plt.plot(data['Perioden'], data['Gehuwd_6'], label='Gehuwd', linestyle='--')
plt.plot(data['Perioden'], data['Ongehuwd_5'], label='Ongehuwd', linestyle='-.')
plt.plot(data['Perioden'], data['Gescheiden_8'], label='Gescheiden', linestyle=':')
plt.title('Burgerlijke staat 1950-2019')
plt.xlabel('Jaar')
plt.ylabel('Aantal')
plt.legend()

subset_2010_2019 = data[(data['Perioden'] >= 2010) & (data['Perioden'] <= 2019)]
plt.subplot(2, 3, 5)
plt.plot(subset_2010_2019['Perioden'], subset_2010_2019['TotaleBevolking_1'], 'y--')
plt.title('Bevolking 2010-2019')
plt.xlabel('Jaar')
plt.ylabel('Bevolking')

plt.tight_layout()
plt.show()
