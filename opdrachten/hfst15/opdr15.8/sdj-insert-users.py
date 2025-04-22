'''Programma voor invoeren users in tabel'''
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

if mysql_db.is_connected():
    print('Connectie met de MySQL server is succesvol!')
    
    mycursor = mysql_db.cursor()
    query = f'''INSERT INTO users (first_name, last_name)
                VALUES
                ('Stefan', 'de Jong'),
                ('Kees', 'Epema'),
                ('Rykle', 'Baron');'''

    mycursor.execute(query)
    mysql_db.commit()
    print('De tabel invoer is succesvol!')
    mysql_db.close()
else:
    print('Helaas geen connectie met de MySQL server!')