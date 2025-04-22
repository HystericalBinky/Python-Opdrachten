'''Programma die voor je rekent'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Schrijf intro naar het scherm

print('''#################################################
Welkom bij rekenen!
Voer twee gehele getallen in.    
''')

# Vraag om getallen via input

Getal1 = input('Geef een eerste getal? ')
Getal2 = input('Geef een tweede getal? ')

# Schrijf ingevulde getallen naar het scherm

print('''''')

print('Getal1 = ' + Getal1)
print('Getal2 = ' + Getal2)

print('''''')

# Zet string om naar integer

intGetal1 = int(Getal1)
intGetal2 = int(Getal2)

# Bereken antwoorden

intSom = intGetal1 + intGetal2
intVerschil = intGetal1 - intGetal2
intVermenigvuldiging = intGetal1 * intGetal2
intDeling = intGetal1 / intGetal2

# Zet antwoorden om naar string

strSom = str(intSom)
strVerschil = str(intVerschil)
strVermenigvuldiging = str(intVermenigvuldiging)
strDeling = str(intDeling)

# Schrijf resultaat naar het scherm

print('De som van ' + Getal1 + ' en ' + Getal2 + ' is ' + strSom)
print('Het verschil van ' + Getal1 + ' en ' + Getal2 + ' is ' + strVerschil)
print('Het product van ' + Getal1 + ' en ' + Getal2 + ' is ' + strVermenigvuldiging)
print('De deling van ' + Getal1 + ' en ' + Getal2 + ' is ' + strDeling)

print('''#################################################
''')

print('Tot ziens!')