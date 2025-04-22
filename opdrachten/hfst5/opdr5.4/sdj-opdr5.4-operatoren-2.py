'''Programma voor antwoorden opdrachten operatoren 2'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak vraag en antwoord variablen aan

aVraag = "a) (5 + 7) / 2                        = 6         <===> "
bVraag = "b) 4 + 4 / 2 + 1                      = 7         <===> "	
cVraag = "c) 2 * 3 / 2                          = 3         <===> "
dVraag = "d) 2 ** 3 - 2                         = 6         <===> "
eVraag = "e) 6 / 3 + 2 * 2                      = 6         <===> "
fVraag = "f) 4 * 3 + (2 - 4)                    = 10        <===> "
gVraag = "g) (2 + 2) - 2 - 9                    = -7        <===> "	

hVraag = "h) 3 <= 4 or 4 == 6                   = True      <===> "
iVraag = "i) 4 != 4 and 5 != 6                  = False     <===> "
jVraag = "j) not ( 4 < 6 and 3 > 4)             = True      <===> "
kVraag = "k) 5 > 6 and 6 <= 7 or 7 < 9          = True      <===> "
lVraag = "l) 5 > 6 and ( 6 <= 7 and 7 < 9 )     = False     <===> "
mVraag = "m) 4 + 2 <= 5 and 2 / 2 != 0          = False     <===> "

aAntwoord = str((5 + 7) / 2)
bAntwoord = str(4 + 4 / 2 + 1)
cAntwoord = str(2 * 3 / 2)
dAntwoord = str(2 ** 3 - 2)
eAntwoord = str(6 / 3 + 2 * 2)
fAntwoord = str(4 * 3 + (2 - 4))
gAntwoord = str((2 + 2) - 2 - 9)

hAntwoord = str(3 <= 4 or 4 == 6)
iAntwoord = str(4 != 4 and 5 != 6)
jAntwoord = str(not ( 4 < 6 and 3 > 4))
kAntwoord = str(5 > 6 and 6 <= 7 or 7 < 9)
lAntwoord = str(5 > 6 and ( 6 <= 7 and 7 < 9 ))
mAntwoord = str(4 + 2 <= 5 and 2 / 2 != 0)

# Print vraag en antwoord variablen op scherm.

print("Vul in de juiste rekenkundige operator: +, -, /, *, ** ?")
print(aVraag + aAntwoord)
print(bVraag + bAntwoord)
print(cVraag + cAntwoord)
print(dVraag + dAntwoord)
print(eVraag + eAntwoord)
print(fVraag + fAntwoord)
print(gVraag + gAntwoord)

print("")

print("Vul in de juiste logische operator: not, or, and ?")

print(hVraag + hAntwoord)
print(iVraag + iAntwoord)
print(jVraag + jAntwoord)
print(kVraag + kAntwoord)
print(lVraag + lAntwoord)
print(mVraag + mAntwoord)