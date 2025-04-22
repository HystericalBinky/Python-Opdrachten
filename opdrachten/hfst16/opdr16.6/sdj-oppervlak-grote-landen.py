'''Programma voor staafdiagram oppervlakte grootste landen'''
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
import seaborn as sns

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="world"
)

cursor = conn.cursor()

query = """
SELECT Name, SurfaceArea
FROM country
ORDER BY SurfaceArea DESC
LIMIT 10;
"""
cursor.execute(query)
data = cursor.fetchall()

landen = [row[0] for row in data]
oppervlakte = [row[1] for row in data]

plt.figure(figsize=(10, 6))
sns.barplot(y=landen, x=oppervlakte, palette="Paired")

plt.title("Tien grootste landen ter wereld", fontsize=14)
plt.xlabel("Oppervlakte (in miljoen km²)", fontsize=12)
plt.ylabel("Landen", fontsize=12)

for index, value in enumerate(oppervlakte):
    plt.text(float(value) + 0.2, index, str(value), va='center', fontsize=10)

plt.legend(landen, title="Landen", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()

cursor.close()
conn.close()