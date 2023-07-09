# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:20:42 2023

@author: Amar Doshi
"""

# Infinite scrolling version


url = 'http://quotes.toscrape.com/js/'


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options


FIREFOXDRIVER_PATH = 'D:\ProgramData\miniconda3\envs\selenium\geckodriver.exe'


service = FirefoxService(executable_path=FIREFOXDRIVER_PATH)

options = Options()

options.add_argument("-headless")
options.page_load_strategy = 'normal'   # eager, none

with webdriver.Firefox(service=service, options=options) as driver:
    driver.get(url)

    quotes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, 'quote')
            )
        )

    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, 'text').text
        author = quote.find_element(By.CLASS_NAME, 'author').text
        tags = ', '.join((quote.find_element(By.CLASS_NAME, 'tags').text.split())[1:])

        print()
        print(f'Quote:\t{text}')
        print(f'Author:\t{author}')
        print(f'Tags:\t{tags}')
