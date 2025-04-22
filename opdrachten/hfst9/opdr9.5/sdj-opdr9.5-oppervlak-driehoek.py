'''Programma voor oppervlak driehoek'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak functie oppervlak_driehoek(lengte, hoogte) aan

def oppervlak_driehoek(lengte = 0, hoogte = 0):
    # Vraag om lengte en hoogte en bewaar die in variabele

    print("Wat is de lengte van de driehoek?")
    lengte = int(input(""))

    print("Wat is de hoogte van de driehoek?")
    hoogte = int(input(""))

    som = (lengte * hoogte) / 2

    print("De oppervlakte van de driehoek is:", som)

oppervlak_driehoek()