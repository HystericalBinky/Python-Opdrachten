'''Programma voor BRM-formule en MET-waarde'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak functies aan

def BMR(age, weight, length, sex):
    """
    Calculate BMR with given values

    Parameters
    ----------
    age : int
        Contains the age the user has given
    weight : int
        Contains the weight the user has given
    length : int
        Contains the length the user has given
    sex : string
        Contains the sex the user has given
    """

    if sex == "m":
        return 88.362 + (13.397 * weight) + (4.799 * length) - (5.677 * age) * 1.2
    elif sex == "v":
        return 447.593 + (9.247 * weight) + (3.098 * length) - (4.33 * age) * 1.2

def MET(age, weight, length, time):
    """
    Calculate MET with given values

    Parameters
    ----------
    age : int
        Contains the age the user has given
    weight : int
        Contains the weight the user has given
    length : int
        Contains the length the user has given
    time : string
        Contains the time the user has given
    """

    return 3 * 3.5 * gewicht / 200 * tijd

loop = True
while loop == True:
    leeftijd = int(input("Wat is uw leeftijd (jaren) ? "))
    gewicht = int(input("Wat is uw gewicht (kg) ? "))
    lengte = int(input("Wat is uw lengte (cm) ? "))
    geslacht = input("Wat is uw geslacht (m/v) ? ")
    tijd = int(input("Hoelang wandelt u per dag (minuten) ? "))

    bmr = int(BMR(leeftijd, gewicht, lengte, geslacht))
    met = int(MET(leeftijd, gewicht, lengte, tijd))
    calories =  bmr + met

    print(f"\nDe totale verbranding per dag is: {calories}\n")

    stop = input("Toets een 'q' om te stoppen ? ")
    if stop == "q":
        print("Tot ziens !")
        exit()
    else:
        stop = ""
        print("")
        continue