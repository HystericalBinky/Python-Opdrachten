'''Programma voor antwoorden opdrachten string methoden 1'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak variable quote aan

quote = '   Eet vriend en vriendin en wordt dronken van liefde.   '

# Maak antwoord variabelen aan

quote_a = "'" + quote + "'"
quote_b = quote.strip()
quote_c = quote_b.upper()
quote_d = quote_b.title()
quote_e = str(len(quote_b))
quote_f = str(quote_b.startswith('e'))
quote_g = str(quote_b.endswith('l'))
quote_h = str(quote_b.count('d'))
quote_i = str(quote_b.count('z'))

# Schrijf antwoorden naar het scherm

print('a) -> quote = ' + quote_a)
print('b) -> ' + quote_b)
print('c) -> ' + quote_c)
print('d) -> ' + quote_d)
print('e) -> ' + quote_e)
print('f) -> ' + quote_f)
print('g) -> ' + quote_g)
print('h) -> ' + quote_h)
print('i) -> ' + quote_i)