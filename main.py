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
    page_load = requests.get(link) #getting the page to load with request module
    p = page_load.content #short variable as a name for content on page
    soup = bs (p, 'html5lib')#parses content using the python html parser

    #Starting the search for needed information
    profile_container = soup.select(".profile")  #finding the profile container on the page
    for results in profile_container:
        artist_title_container = results.find_all('span')
        artist = artist_title_container[1].find('a').string
        title = artist_title_container[2].string.lstrip().rstrip()
    print(artist)
    print(title)



if __name__ == "__main__":
    main()
