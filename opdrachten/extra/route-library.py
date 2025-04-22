import json

class Lokaal:
    def __init__(self, naam, richting):
        self.naam = naam
        self.richting = richting

    def summary(self):
        print(f"Naam: {self.naam}")
        print(f"Richting: {self.richting}")

lokalen = [Lokaal("C1.13", "west"), Lokaal("C1.04", "west"), Lokaal("C1.06", "west")]

for lokaal in lokalen:
    lokaal.summary()

with open("route-data.json", "w") as outfile:
    json.dump([vars(lokaal) for lokaal in lokalen], outfile, indent=4)