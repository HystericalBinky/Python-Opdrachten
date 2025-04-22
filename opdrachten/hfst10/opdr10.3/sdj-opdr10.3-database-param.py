'''Programma voor database param'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak functie print_dic(**dictionary) aan

def print_dic(**dictionary):
    """
    Print all of the information in the dictionary

    Parameters
    ----------
    arguments : dictionary
        Contains the dictionary given
    """

    for key in dictionary:
        print(f"{key} : {dictionary.get(key)}")

print_dic(gebruikersnaam ="root", 
          wachtwoord ="",  
          ip_adres ="127.0.0.1",
          poort =1433) 