'''Programma voor temp tuple'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak tuple temp aan

temp = (22.7, 30.8, 26.8, 19.3, 16.7, 38.9, 32.5, 27.5, 24.5)

# Schrijf antwoorden naar het scherm

print(f"a) Max: {max(temp)}")
print(f"b) Min: {min(temp)}")
print(f"c) Aantal: {len(temp)}")

vermenigvuldigd = 1
for waarde in temp: 
    vermenigvuldigd *= waarde 

print(f"d) Vermenigvuldig alles: {vermenigvuldigd}")
print(f"e) Nieuw: {temp[2:-2]}")