# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 17:29:10 2023

@author: Amar Doshi
"""


base_url = url = 'http://books.toscrape.com/'


import csv
import requests
from bs4 import BeautifulSoup

from time import sleep

headers = {'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'}

ratings = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

with open('Books.csv', 'w', encoding="utf-8", newline='') as f:
    w = csv.writer(f)

    w.writerow(('Title', 'Price £', 'Rating', 'Availability', 'URL'))

    while url:
        print()
        print(url)

        page = requests.get(url, headers=headers)

        if page.ok:
            soup = BeautifulSoup(page.content, 'html.parser')

            books = soup.body.find_all('article', class_='product_pod')

            for book in books:
                title = book.h3.a['title']
                price = book.find('p', class_="price_color").text[1:]
                rating = ratings.get(book.p['class'][1], -1)
                avl = (''.join(book.find('p', class_='instock availability')
                                .text.splitlines())).strip()
                book_url = book.h3.a['href']

                w.writerow((title, price, rating, avl, book_url))

            next_page = soup.body.find('li', class_='next')
        else:
            next_page = None

        if next_page:
            url = base_url + next_page.a['href']
            base_url = 'http://books.toscrape.com/catalogue/'
            sleep(1)
        else:
            url = None


# if __name__ == '__main__':

