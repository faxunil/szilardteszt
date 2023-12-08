from bs4 import BeautifulSoup
import requests
import re

page_to_scrape = requests.get("https://arfigyelo.gvh.hu/kereses/toj%C3%A1s?order=relevance")
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
termek = soup.findAll('div', attrs={'class':'card-title'})

if page_to_scrape.status_code == 200:
    print("Az oldal sikeresen letöltve.")
else:
    print(f"Hiba a letöltés során. Státuszkód: {page_to_scrape.status_code}")
    exit()

print(termek)

num = 0

for item in termek:
    y = item.text
    x = re.search("10", item.text)
    if x:
        print('------------------------------------------------------------------------------')
        print(y)
        print('------------------------------------------------------------------------------')
        print('\n')
        num = num + 1

print(f'Találat: {num}')
