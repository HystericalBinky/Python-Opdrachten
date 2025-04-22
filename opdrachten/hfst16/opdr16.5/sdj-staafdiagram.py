'''Programma voor staafdiagram'''
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
SELECT Name, LifeExpectancy
FROM country
WHERE LifeExpectancy IS NOT NULL
ORDER BY LifeExpectancy ASC
LIMIT 10;
"""
cursor.execute(query)
data = cursor.fetchall()

landen = [row[0] for row in data]
levensverwachting = [row[1] for row in data]

plt.figure(figsize=(10, 6))
sns.barplot(x=landen, y=levensverwachting, palette="pastel")

plt.title("Tien landen met de laagste levensverwachting", fontsize=14)
plt.xlabel("Land", fontsize=12)
plt.ylabel("Leeftijd", fontsize=12)
plt.xticks(rotation=45)

plt.show()

cursor.close()
conn.close()
