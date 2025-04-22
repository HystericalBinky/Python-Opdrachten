'''Programma voor grafiek criminaliteit VS'''
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
    database="fbi-crimes"
)

cursor = db.cursor()

query = """
SELECT year, robbery, aggravated_assault, burglary
FROM fbi_crimes
ORDER BY year ASC
"""
cursor.execute(query)

results = cursor.fetchall()

cursor.close()
db.close()

years = [row[0] for row in results]
robbery = [row[1] for row in results]
aggravated_assault = [row[2] for row in results]
burglary = [row[3] for row in results]

plt.figure(figsize=(12, 6))

plt.plot(years, robbery, marker='s', linestyle='-', color='blue', label='rooftoestellen')
plt.plot(years, aggravated_assault, marker='o', linestyle='-', color='orange', label='mishandeling')
plt.plot(years, burglary, marker='^', linestyle='-', color='green', label='inbraken')

plt.title("Criminaliteit VS periode 1999-2018", fontsize=16)
plt.xlabel("Jaar", fontsize=12)
plt.ylabel("Aantal (in miljoenen)", fontsize=12)

plt.legend(fontsize=10, loc='best')

plt.xticks(years, rotation=45)

plt.grid(visible=True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
