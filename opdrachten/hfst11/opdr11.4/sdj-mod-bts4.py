'''Programma voor Module beautifulsoup4'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

from bs4 import BeautifulSoup
with open("opdrachten\hfst11\opdr11.4\scraper-website\scraper.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(f"1. {soup.title.string}")
print(f"2. {soup.script}")
print("3.")
for link in soup.find_all('a'):
    print(link.get('href'))
print("4.")
for article in soup.find_all('article'):
    for p in article.find_all('p'):
        print(p.string)
print("5.")
for article in soup.find_all('article'):
    for link in article.find_all('a'):
            print(link.get('href'))
    for p in article.find_all('p'):
        print(p.string)
print("6.")
text = soup.get_text()
print(text[:1000])
print("7.")
for css in soup.find_all("link"):
    if css.attrs.get("href"):
        url = "opdrachten/hfst11/opdr11.4/scraper-website/"
        css_url = url + css.attrs.get("href")
        with open(css_url) as file:
            readFile = file.read()
            print(readFile)
