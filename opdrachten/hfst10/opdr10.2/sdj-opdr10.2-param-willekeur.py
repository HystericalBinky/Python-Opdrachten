'''Programma voor param willekeur'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak functie som_gem(*arguments) aan

def som_gem(*arguments):
    """
    Calculate the sum and average of any amount of numbers

    Parameters
    ----------
    arguments : list
        Contains all the numbers given
    """

    Som = 0

    for arg in arguments:
        Som += arg
    
    Gem = Som / len(arguments)

    Som = round(Som, 1)
    Gem = round(Gem, 1)
    
    print(f"Lijst: {arguments}")
    print(f"Som: {Som}")
    print(f"Gem: {Gem}")

som_gem( 1, 2, 3 )
print("")
som_gem( 7, 66, 94, 73, 12, 9, 33, 21 )
print("")
som_gem( 3, -79, 34, 47, 19, 8 )