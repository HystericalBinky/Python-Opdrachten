'''Programma voor cm naar inch, feet'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak lambda functies aan

cminch = lambda cm : int(cm) / 2.54
inchfeet = lambda inch : int(inch) / 12.0
cmfeet = lambda cm : (int(cm) / 2.54) / 12.0

# Maak functie schrijf_tabel_meet(*range) aan

def schrijf_table_meet(range):
    """
    Caculate cm to inch and feet, and print result in table

    Parameters
    ----------
    arguments : range
        Contains the range of numbers given
    """

    column = 1
    print(f"CM \t INCH \t FEET \tCM \t INCH \t FEET \tCM \t INCH \t FEET \tCM \t INCH \t FEET \tCM \t INCH \t FEET")
    for number in range:
        if column <5:
            print(f"{number} \t {round(cminch(number), 2)} \t {round(cmfeet(number), 1)} \t", end="")
            column += 1
        else:
            print(f"{number} \t {round(cminch(number), 2)} \t {round(cmfeet(number), 1)}")
            column = 1

schrijf_table_meet(range(100, 201))