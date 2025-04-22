'''Programma voor updaten users in tabel'''
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

host = 'localhost'
port = 3306
user = 'root'
password = ''

mysql_db = mysql.connector.connect(
    host = host,
    port = port,
    user = user,
    password = password,
    database = 'db-python'
)

mycursor = mysql_db.cursor()

if mysql_db.is_connected():
    print('Connectie met de MySQL server is succesvol!')

    def zoek_gebruiker(zoekterm):
        query = "SELECT id, first_name, last_name FROM users WHERE first_name LIKE %s OR last_name LIKE %s"
        mycursor.execute(query, (f"%{zoekterm}%", f"%{zoekterm}%"))
        resultaten = mycursor.fetchall()

        if not resultaten:
            print("\nGeen gebruiker met die naam gevonden!")
            return None

        for idx, (user_id, first_name, last_name) in enumerate(resultaten, start=1):
            print(f"{idx}: {first_name} {last_name} (ID: {user_id})")

        keuze = input("\nKies het nummer van de gebruiker om te updaten (Enter om te annuleren): ")
        if not keuze.isdigit() or not (1 <= int(keuze) <= len(resultaten)):
            return None

        return resultaten[int(keuze) - 1][0]  # Geeft het ID terug

    def update_gebruiker(user_id):
        nieuwe_voornaam = input("\nGeef een nieuwe voornaam (Enter om over te slaan): ").strip()
        nieuwe_achternaam = input("\nGeef een nieuwe achternaam (Enter om over te slaan): ").strip()

        if nieuwe_voornaam:
            mycursor.execute("UPDATE users SET first_name = %s WHERE id = %s", (nieuwe_voornaam, user_id))
        if nieuwe_achternaam:
            mycursor.execute("UPDATE users SET last_name = %s WHERE id = %s", (nieuwe_achternaam, user_id))

        mysql_db.commit()
        print("\nGebruiker succesvol geüpdatet!")

        mysql_db.close()
    
    zoekterm = input("\nZoek op een naam om up te daten: ").strip()
    user_id = zoek_gebruiker(zoekterm)
    
    if user_id:
        update_gebruiker(user_id)

    print("\nTot ziens!")
else:
    print('Helaas geen connectie met de MySQL server!')