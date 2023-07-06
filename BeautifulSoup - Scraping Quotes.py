# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 19:02:15 2023

@author: Amar Doshi
"""

'''
Using requests and BeautifulSoup for scraping quotes data
'''

import csv
import requests
from bs4 import BeautifulSoup

from time import sleep


url = base_url = 'https://quotes.toscrape.com'

with open('Quotes.csv', 'w', encoding="utf-8", newline='') as f:
    w = csv.writer(f)

    w.writerow(('Text', 'Author', 'Keywords'))

    while url:
        print()
        print(url)

        page = requests.get(url)

        if page.ok:
            soup = BeautifulSoup(page.content, 'html.parser')

            quotes = soup.body.find_all('div', class_='quote')

            for quote in quotes:
                text = quote.find('span', class_='text').text
                author = quote.find('small', class_="author").text
                keywords = quote.div.meta['content']

                w.writerow((text, author, keywords))

            next_page = soup.body.nav.ul.find('li', class_='next')
        else:
            next_page = None

        if next_page:
            url = base_url + next_page.a['href']
            sleep(2)
        else:
            url = None


# if __name__ == '__main__':
