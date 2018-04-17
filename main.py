#!/usr/bin/python

import time
from bs4 import BeautifulSoup as bs
import requests

def main():
    print('Welcome to the Discog Vinyl Scrapper.')
    print('Give us a moment to set up')
    time.sleep(3)
    link = input ('Please input your link: ')

    get_info(link)

def get_info(link):
    page_load = requests.get(link) #getting the page to load with request modul
    p = page_load.content #short variable as a name for content on page
    soup = bs (p, 'html.parser')

if __name__ == "__main__":
    main()
