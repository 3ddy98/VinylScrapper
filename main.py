#!usr/bin/python

import time
from bs4 import BeautifulSoup as bs
import requests

def main():
    #link = input('Please enter Vinyl Profile Link: ')
    link = 'https://www.discogs.com/Dexys-Midnight-Runners-Emerald-Express-Come-On-Eileen/release/3151574'
    page = requests.get(link) #requests the webpage
    soup = bs(page.content,'lxml') #parses the website with lxml framerwork
    name_container = soup.find('meta',itemprop='name') #finds meta container with name of artist and vinyl
    full_title = name_container['content']
    title_and_songname = full_title.rsplit('-')
    title = title_and_songname[0]
    song_name = title_and_songname[1].replace(' ','',1)



if __name__ == "__main__":
    main()
