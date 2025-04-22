'''Programma voor berekenen fahrenheit en kelvin'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Vraag om getal en bewaar die in variabele

print("Geef de temperatuur in graden celsius.")
celsiusStr = input("")

celsiusFloat = float(celsiusStr)

# Bereken fahrenheit en kelvin in variabele

fahrenheitFloat = (celsiusFloat * 9 / 5) + 32.0, 0
kelvinFloat = celsiusFloat + 273.15

fahrenheitStr = str(fahrenheitFloat)
kelvinStr = str(kelvinFloat)

# Print resultaat op scherm.

print("")
print("Celsius      = " + celsiusStr + "°C")
print("Fahrenheit   = " + fahrenheitStr + "°F")
print("Kelvin       = " + kelvinStr + "°K")