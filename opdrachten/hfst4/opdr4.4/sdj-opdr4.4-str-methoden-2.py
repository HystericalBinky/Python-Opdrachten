'''Programma voor antwoorden opdrachten string methoden 2'''
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

quote = "Het leven is als rijden op een bromfiets. Je moet in beweging blijven om niet om te vallen."
lenQuote = len(quote) - 1

# Maak antwoord variabelen aan

quote_a = "'" + quote + "'"
quote_b = quote.replace("bromfiets", "fiets")
quote_c = quote_b.replace("beweging", "balans")

lenQuoteC = len(quote_c)

quote_d = quote[2]
quote_e = quote[-2]
quote_f = quote[4:9]
quote_g = quote[0:9]
quote_h = quote[lenQuote - 12:lenQuote + 1]
quote_i = quote[:lenQuote:2]
quote_j = quote[62:70:3]
quote_k = quote_c[0:lenQuoteC - 7]
quote_l = quote_c[4:lenQuoteC]
quote_m = quote_c[13:lenQuote - 27]
quote_n = quote_c[::-1]

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
print('j) -> ' + quote_j)
print('k) -> ' + quote_k)
print('l) -> ' + quote_l)
print('m) -> ' + quote_m)
print('n) -> ' + quote_n)