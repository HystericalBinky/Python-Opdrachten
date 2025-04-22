'''Programma voor HTML-5 template'''
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

taal = ""
auteur = ""
titel = ""
beschrijving = ""

# Maak functie html5_template(taal, auteur, titel, omschrijving) aan

def html5_template(language, author, title, description):
    """
    Caculate cm to inch and feet, and print result in table

    Parameters
    ----------
    language : string
        Contains the language the user has given
    author : string
        Contains the author the user has given
    title : string
        Contains the title the user has given
    description : string
        Contains the description the user has given
    """

    print(f'\n################################################\nHtml pagina\n\n\t\t<!DOCTYPE html>\n\t\t<html lang="{language}>\n\t\t\t<head>\n\t\t\t\t<title>{title}</title>\n\t\t\t\t<meta charset="">\n\t\t\t\t<meta viewport="width=device-width, initial-scale=1">\n\t\t\t\t<meta name="description" content="{description}">\n\t\t\t\t<meta name="author" content="{author}"\n\t\t\t</head>\n\t\t\t<body>\n\n\t\t\t\t<h3> Welkom </h3>\n\t\t\t\t<p> Dit is de homepage van {author} ! </p>\n\n\t\t\t</body>\n\t\t</html>\n################################################')

print(f"Welkom bij HTML5 template !\nDruk 'q'of 'Q' om het programma af te sluiten\n")

valideTaal = False
while valideTaal == False:
    print(f"Wat is de taal van de pagina ?")
    taal = input("Kies uit één van de volgende talen: nl, en, de, be ? ")

    if taal == "nl":
        valideTaal == True
        break
    elif taal == "en":
        valideTaal == True
        break
    elif taal == "de":
        valideTaal == True
        break
    elif taal == "be":
        valideTaal == True
        break
    elif taal == "q":
        exit()
    elif taal == "Q":
        exit()
    else:
        continue  

print(f"\nWat is de karakterset van de pagina ?")
karakterset = input("Druk op <enter> voor een default waarde ")

print(f"\nWat is de viewport van de pagina ?")
viewport = input("Druk op <enter> voor een default waarde ")

while auteur == "":
    print(f"\nWie is de auteur van de pagina ?")
    auteur = input("")

    if auteur == "q":
        exit()
    elif auteur == "Q":
        exit()

while titel == "":
    print(f"\nWat is de titel van de pagina ?")
    titel = input("")

    if titel == "q":
        exit()
    elif titel == "Q":
        exit()

while beschrijving == "":
    print(f"\nWat is de omschrijving van de pagina ?")
    beschrijving = input("")

    if beschrijving == "q":
        exit()
    elif beschrijving == "Q":
        exit()

print(f"\nGeef hier de inhoud van de pagina ?")
inhoud = input("Druk op <enter> voor een default waarde ")

html5_template(taal, auteur, titel, beschrijving)