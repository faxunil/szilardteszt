from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime

driver = webdriver.Chrome()

driver.get('https://arfigyelo.gvh.hu/kereses/toj%C3%A1s?order=relevance')

sleep(1)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

termek = soup.find_all('div', 'col')
    
num = 0

print(f'Dátum: {datetime.date.today()}')

for x in termek:
    title = x.find('div', 'card-title')
    store = x.find_all('div', 'store-name')
    prices = x.find_all('span', 'price-amount')
    uprices = x.find_all('div', 'popover__inner-unit-amount')
    if title is not None:
        num += 1
        print(f'{num} {title.text}')
        for u, p, up in zip(store, prices, uprices):
            if u is not None and u.text.strip() and p is not None and p.text.strip():
                print(f'   Üzlet: {u.text.strip()}  Ár: {p.text.strip()}    Egységár: {up.text.strip()}')
