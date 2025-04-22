'''Programma voor vraag 1'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

loop = True
while loop == True:
    print("Programma berekenen \n")

    print("Kies uit: +, -, *, /.")
    rekenTeken = input("")

    print("Geef een (geheel) getal.")
    getal1 = input("")

    valideGetal2 = False
    while valideGetal2 == False:
        print("Geef een (geheel) getal.")
        getal2 = input("")

        if rekenTeken == "/":
            if getal2 == "0":
                valideGetal2 = False
            else:
                valideGetal2 = True
                break
        else:
            valideGetal2 = True
            break
    
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y}
    
    print(f"Resultaat van {getal1} {rekenTeken} {getal2} is {operators[rekenTeken](int(getal1),int(getal2))} \n")

    print("Type een willekeurige toets om door te gaan...")
    print("Kies 's' om te stoppen...")
    stop = input("")

    if stop == "s":
        exit()
    else:
        stop = ""
        continue