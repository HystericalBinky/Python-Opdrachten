'''Programma voor berekenen fahrenheit'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak variabelen aan

celsius = -10

while celsius <= 10:
    fahrenheit = (celsius * 9 / 5) + 32.0
    
    print("Celsius: " + str(celsius) + " °C is " + str(fahrenheit) + " °F")

    celsius += 1