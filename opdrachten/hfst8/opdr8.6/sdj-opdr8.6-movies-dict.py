'''Programma voor movies dic'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

# Maak dic movies aan

movies = [
    { "titel"       : "The Godfather",
      "jaar"        : 1972,
      "cijfer"      : 9.2,
      "regisseur"   : "Francis Ford Coppola" },
    
    { "titel"       : "The Shawshank Redemption",
      "jaar"        : 1994,
      "cijfer"      : 9.3,
      "regisseur"   : "Frank Darabont" },
    
    { "titel"      : "Schindler's List",
      "jaar"       : 1993,
      "cijfer"     : 8.9,
      "regisseur"  : "Steven Spielberg" },

    { "titel"      : "Raging Bull",
      "jaar"       : 1980,
      "cijfer"     : 8.2,
      "regisseur"  : "Martin Scorsese" },

    { "titel"      : "Casablanca",
       "jaar"      : 1942,
       "cijfer"    : 8.5,
       "regisseur" : "Michael Curtiz" }
]

# Schrijf antwoorden naar het scherm

print("a) Alle film titels")
for dic in movies:
    print(dic.get("titel"))

print("")

print("b) Alle films voor 1990")
for dic in movies:
    if dic.get("jaar") < 1990:
        print(f"{dic.get("titel")} : {dic.get("jaar")}")

print("")

print("c) Film(s) van Steven Spielberg")
for dic in movies:
    if dic.get("regisseur") == "Steven Spielberg":
        for key in dic:
            print(f"{key}: {dic.get(key)}")

print("")

highestScore = 0
highestScoredMovie = ""

for dic in movies:
    if dic.get("cijfer") > highestScore:
        highestScore = dic.get("cijfer")
        highestScoredMovie = dic.get("titel")

print("d) Film hoogste beoordeling")

for dic in movies:
    if dic.get("titel") == highestScoredMovie:
        for key in dic:
            print(f"{key}: {dic.get(key)}")

print("")

print("e) Gesorteed op jaartal van oud naar nieuw")

newMoviesList = sorted(movies, key=lambda d: d['jaar'])

for dic in newMoviesList:
    for key in dic:
        print(f"{key}: {dic.get(key)}")
    print("")