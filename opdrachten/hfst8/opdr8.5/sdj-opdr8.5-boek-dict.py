'''Programma voor boek dic'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak dic fav_boek aan

fav_boek = {
    "titel"     : "Guns, germs and steel",
    "subtitel"  : "The Fates of Human Societies.",
    "schrijver" : "Jared Diamond",
    "jaar"      : 2007,
    "uitgever"  : "Ww Norton & Co"
}

print(f"fav_boek = {fav_boek}")

# Schrijf antwoorden naar het scherm

fav_boek.update({"jaar": 1997})

print(f"a) {fav_boek}")

fav_boek["isbn"] = "0-393-03891-2"

print(f"b) {fav_boek}")

fav_boek.pop("subtitel")

print(f"c) {fav_boek}")
print(f"d) {fav_boek.get("uitgever")}")
print("e) ")

for key in fav_boek:
    print(f"{key}: {fav_boek.get(key)}")