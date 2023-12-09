from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get('https://arfigyelo.gvh.hu/kereses/toj%C3%A1s?order=relevance')

sleep(2)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

termek = soup.find_all('div', 'col')

num = 0

for x in termek:
    title = x.find('div', 'card-title')
    prices = x.find_all('div', 'price-row')
    if title is not None:
        num += 1
        print(f'{num} {title.text}')
        for price in prices:
            if price is not None and price.text.strip():
                print(f'   Ár: {price.text.strip()}')
