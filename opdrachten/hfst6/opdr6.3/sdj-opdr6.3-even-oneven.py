'''Programma voor even of oneven'''
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

print("Geef een geheel getal")
getalStr = input("")

getalInt = int(getalStr)

# Check of getal even of oneven is en print resultaat

if getalInt % 2 == 0:
    print("Het ingevoerde getal:", getalInt, "is even.")
else:
    print("Het ingevoerde getal:", getalInt, "is oneven.")