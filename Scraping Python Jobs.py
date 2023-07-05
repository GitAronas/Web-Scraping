# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 15:27:51 2023

@author: Amar Doshi
"""

'''
Use requests and Beautiful Soup for scraping and parsing data
from a demo website.
'''

import csv
import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'

page = requests.get(url)

if page.ok:
    soup = BeautifulSoup(page.content, 'html.parser')

    jobs = soup.findAll('div', class_='card-content')

    with open('jobs_list.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Company', 'Location'])

        for job in jobs:
            title = job.find('h2', class_='title').text.strip()
            company = job.find('h3', class_='company').text.strip()
            location = job.find('p', class_='location').text.strip()

            if 'python' in title.lower():
                writer.writerow([title, company, location])
