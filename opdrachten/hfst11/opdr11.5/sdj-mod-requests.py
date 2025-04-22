'''Programma voor Module requests'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

import requests
from bs4 import BeautifulSoup

url = "https://www.goodreads.com/quotes"

request_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=request_headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quoteText")
    
    print("1.")
    for quote in quotes[:3]:
        text = quote.get_text(strip=True, separator=" ").split("―")
        quote_text = text[0].strip()
        author = text[1].strip() if len(text) > 1 else "Onbekend"
        print(f"Quote: {quote_text}")
        print(f"Bedenker: {author}")
        print()

    print("2.")
    for quote in quotes[-2:]:
        text = quote.get_text(strip=True, separator=" ").split("―")
        quote_text = text[0].strip()
        author = text[1].strip() if len(text) > 1 else "Onbekend"
        print(f"Quote: {quote_text}")
        print(f"Bedenker: {author}")
        print()

    print("3.")
    footer_links = soup.find_all("a", href=True)
    social_platforms = ["facebook", "twitter", "instagram", "linkedin"]
    for link in footer_links:
        href = link["href"].strip()
        if any(platform in href for platform in social_platforms):
            print(href)
else:
    print("Could not connect to website. Statuscode:", response.status_code)
