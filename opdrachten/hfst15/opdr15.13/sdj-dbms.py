'''Programma voor menu DBMS'''
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

    def toon_gebruikers():
        """ Toont alle gebruikers in de database. """
        mycursor.execute("SELECT id, first_name, last_name FROM users")
        gebruikers = mycursor.fetchall()

        if not gebruikers:
            print("Geen gebruikers gevonden.")
        else:
            print("\nGebruikerslijst:")
        for user in gebruikers:
            print(f"ID: {user[0]} | {user[1]} {user[2]}")

    def voeg_gebruiker_toe():
        """ Voegt een nieuwe gebruiker toe aan de database. """
        voornaam = input("\nGeef een voornaam: ").strip()
        achternaam = input("Geef een achternaam: ").strip()

        if voornaam and achternaam:
            mycursor.execute("INSERT INTO users (first_name, last_name) VALUES (%s, %s)", (voornaam, achternaam))
            mysql_db.commit()
            print("\nGebruiker succesvol toegevoegd!")
        else:
            print("\nVoor- en achternaam mogen niet leeg zijn.")

    def zoek_gebruiker():
        """ Zoekt een gebruiker op voor- of achternaam. """
        zoekterm = input("\nZoek op een naam: ").strip()
        mycursor.execute("SELECT id, first_name, last_name FROM users WHERE first_name LIKE %s OR last_name LIKE %s",
                    (f"%{zoekterm}%", f"%{zoekterm}%"))
        resultaten = mycursor.fetchall()

        if not resultaten:
            print("\nGeen gebruikers gevonden met die naam.")
        else:
            print("\nGevonden gebruikers:")
        for user in resultaten:
            print(f"ID: {user[0]} | {user[1]} {user[2]}")

    def update_gebruiker():
        """ Werk een gebruiker bij op basis van ID. """
        toon_gebruikers()
        user_id = input("\nVoer het ID van de gebruiker in die u wilt updaten: ").strip()

        mycursor.execute("SELECT first_name, last_name FROM users WHERE id = %s", (user_id,))
        user = mycursor.fetchone()

        if not user:
            print("\nGeen gebruiker gevonden met dit ID.")
            return

        print(f"\nHuidige naam: {user[0]} {user[1]}")
        nieuwe_voornaam = input("\nNieuwe voornaam (Enter voor geen wijziging): ").strip() or user[0]
        nieuwe_achternaam = input("Nieuwe achternaam (Enter voor geen wijziging): ").strip() or user[1]

        mycursor.execute("UPDATE users SET first_name = %s, last_name = %s WHERE id = %s", 
                   (nieuwe_voornaam, nieuwe_achternaam, user_id))
        mysql_db.commit()
        print("\nGebruiker succesvol geüpdatet!")

    def verwijder_gebruiker():
        """ Verwijder een gebruiker op basis van ID. """
        toon_gebruikers()
        user_id = input("\nVoer het ID van de gebruiker in die u wilt verwijderen: ").strip()

        mycursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = mycursor.fetchone()

        if not user:
            print("\nGeen gebruiker gevonden met dit ID.")
            return

        bevestiging = input(f"\nWeet u zeker dat u {user[1]} {user[2]} wilt verwijderen? (y/n): ").strip().lower()
        if bevestiging == 'y':
            mycursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            mysql_db.commit()
            print("\nGebruiker succesvol verwijderd!")
        else:
            print("\nVerwijderen geannuleerd.")

    """ Hoofdmenu van het programma. """
    while True:
        print("\n########################################################")
        print("1:  Schrijf alle gebruikers naar het scherm")
        print("2:  Voeg een gebruiker toe")
        print("3:  Zoek een gebruiker")
        print("4:  Update een gebruiker")
        print("5:  Verwijder een gebruiker")
        print("X:  Programma afsluiten")
        print("########################################################")
        keuze = input("\nWat wilt u doen? \nKies uit: 1, 2, 3, 4, 5 of X? \n? $> ").strip().lower()

        if keuze == "1":
            toon_gebruikers()
        elif keuze == "2":
            voeg_gebruiker_toe()
        elif keuze == "3":
            zoek_gebruiker()
        elif keuze == "4":
            update_gebruiker()
        elif keuze == "5":
            verwijder_gebruiker()
        elif keuze == "x":
            print("\nProgramma afgesloten. Tot ziens!")
            break
        else:
            print("\nOngeldige keuze. Probeer opnieuw.")
else:
    print('Helaas geen connectie met de MySQL server!')