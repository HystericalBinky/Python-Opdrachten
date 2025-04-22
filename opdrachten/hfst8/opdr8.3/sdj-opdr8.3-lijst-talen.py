'''Programma voor lijst talen'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak lijst vakkenlijst aan

vakkenlijst = [ "JavaScript", "Python", "HTML", "CSS", "LiveScript", "PHP", "EcmaScript"]

# Schrijf antwoorden naar het scherm

print(f"a) {vakkenlijst}")
print(f"b) {len(vakkenlijst)}")
print(f"c) {vakkenlijst[1]}")

vakkenlijst.sort()

print(f"d) {vakkenlijst}")

vakkenlijst.remove("LiveScript")

print(f"e) {vakkenlijst}")

vakkenlijst.pop(4)

print(f"f) {vakkenlijst}")

vakkenlijst.remove("EcmaScript")
vakkenlijst.insert(1, "ES6")

print(f"g) {vakkenlijst}")

vakkenlijstSplice1 = vakkenlijst[0:2]
vakkenlijstSplice2 = vakkenlijst[4:]

vakkenlijstSpliced = vakkenlijstSplice1 + vakkenlijstSplice2

print(f"h) {vakkenlijstSpliced}")
print(f"i) {[x.lower() for x in vakkenlijstSpliced]}")