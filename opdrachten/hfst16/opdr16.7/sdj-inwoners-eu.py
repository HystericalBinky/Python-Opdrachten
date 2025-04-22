'''Programma voor cirkeldiagram inwoners europa'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

import mysql.connector
import matplotlib.pyplot as plt

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="world"
)

cursor = db.cursor()

query = """
SELECT Name, Population 
FROM Country
WHERE Continent = 'Europe' AND Population > 15000000
"""
cursor.execute(query)

results = cursor.fetchall()

cursor.close()
db.close()

countries = [row[0] for row in results]
populations = [row[1] for row in results]

plt.figure(figsize=(8, 8))
plt.pie(
    populations,
    labels=[f"{country}\n{pop/1e6:.1f}mln" for country, pop in zip(countries, populations)],
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 10}
)
plt.title("Inwoners Europa met meer dan 15 miljoen inwoners", fontsize=14)
plt.tight_layout()

plt.show()
