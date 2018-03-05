import time
from bs4 import BeautifulSoup as bs
import requests
import time
import csv

def main():

    print('Please wait 3 seconds while we warm things up...\n')#This is meant to keep the script from being blocked on website
    time.sleep(3)

    #link = input('Please enter Vinyl Profile Link: ')
    link = 'https://www.discogs.com/Dexys-Midnight-Runners-Emerald-Express-Come-On-Eileen/release/3151574'
    page = requests.get(link) #requests the webpage
    soup = bs(page.content,'lxml') #parses the website with lxml framerwork
    name_container = soup.find('meta',itemprop='name') #finds meta container with name of artist and vinyl

    full_title = name_container['content']
    title_and_songname = full_title.rsplit('-')
    artist = title_and_songname[0]
    vinyl = title_and_songname[1].replace(' ','',1)

    print('Artist: ', artist)
    print('Song  : ', vinyl)
    print('This will close in 10 seconds')
    print('You should now have results gathered in your excel file')
    time.sleep(10)

def csv_export(artist, vinyl, link,):
    print('something')


if __name__ == "__main__":
    main()
