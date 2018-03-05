import time
from bs4 import BeautifulSoup as bs
import requests
import time
import csv
import msvcrt

def main():

    print('Please wait 3 seconds while we warm things up...\n')#This is meant to keep the script from being blocked on website
    time.sleep(3)

    link = input('Please enter Vinyl Profile Link: ')
    #link = 'https://www.discogs.com/Dexys-Midnight-Runners-Emerald-Express-Come-On-Eileen/release/3151574'
    page = requests.get(link) #requests the webpage
    soup = bs(page.content,'lxml') #parses the website with lxml framerwork
    name_container = soup.find('meta',itemprop='name') #finds meta container with name of artist and vinyl

    full_title = name_container['content'] #extracts data from meta container but has Artist and Vinyl in same string
    title_and_songname = full_title.rsplit('-')# splits Artist and Vinyl into two strings

    artist = title_and_songname[0] # assigning Artist string
    vinyl = title_and_songname[1].replace(' ','',1)# assigning vinyl string
    release_year = 'tbd' #havent gotten the date gathering feature going yet

    print('Artist: ', artist)
    print('Vinyl : ', vinyl)

    csv_export(artist,vinyl,link,release_year)
    #print('You should now have results gathered in your csv file')
    print('Press any key to exit...')

    msvcrt.getch()#leaves the window open for 10 seconds by sleeping and not doing anything

def csv_export(artist,vinyl,link,release_year):
    print('')


if __name__ == "__main__":
    main()
