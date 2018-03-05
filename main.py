import time
from bs4 import BeautifulSoup as bs
import requests
import time
import csv
import datetime

def main():

    print('Please wait 3 seconds while we warm things up...\n')#This is meant to keep the script from being blocked on website
    checked_date = datetime.datetime.now().strftime("%m/%d/%Y");
    time.sleep(3)

    link = input('Please enter Vinyl Profile Link: ')
    condition = input('Please enter condition: ')
    #link = 'https://www.discogs.com/Dexys-Midnight-Runners-Emerald-Express-Come-On-Eileen/release/3151574'
    page = requests.get(link) #requests the webpage
    soup = bs(page.content,'html.parser') #parses the website with lxml framerwork

    artist,vinyl,release_date,label,cat_number = info_extract(soup,link)
    print('Artist   : ', artist) #Done
    print('Vinyl    : ', vinyl) #Done
    print('Checked  : ', checked_date)
    print('Condition: ', condition)
    print('CAT #    : ', cat_number)
    print('Released : ', release_date) #Done
    print('Label    : ', label)
    print('Link     : ', link)

    #CALLING EXPORT MACHINE MUAHAHAH
    csv_export(artist,vinyl,checked_date,condition,cat_number,release_date,label,link)
    #print('You should now have results gathered in your csv file')
    print('Press any key to exit...')

    time.sleep(3)

def info_extract(soup,link):
    #DATE EXTRACTION STARTS HERE
    for info in soup.find_all('div',{'class':'profile'}):
        content = info.find_all('div',{'class':'content'})
        if (content[3].a != None):
            release_year = content[3].a.string.lstrip().rstrip()

        else:
            release_year = 'N/A'

        if(content[0].a != None):
            label = content[0].a.string.lstrip().rstrip()
            cat_number_temp = content[0].a.next_sibling.split(' ',2)
            cat_number = cat_number_temp[2].rstrip()

        else:
            label = 'N/A'
            cat_number = 'N/A'


    #ARTIST AND VINYL EXTRACTION STARTS HERE
    name_container = soup.find('meta',itemprop='name')
    if name_container == None:
        name_container = soup.find('meta',{'property':'og:title'}) #finds meta container with name of artist and vinyl

    full_title = name_container['content'] #extracts data from meta container but has Artist and Vinyl in same string

    title_and_songname = full_title.rsplit('-')# splits Artist and Vinyl into two strings

    artist = title_and_songname[0] # assigning Artist string
    vinyl = title_and_songname[1].replace(' ','',1)# assigning vinyl string

    #csv_export(artist,vinyl,link,release_year)
    return(artist,vinyl,release_year,label,cat_number)

def csv_export(artist,vinyl,checked_date,condition,cat_number,release_date,label,link):
    with open('Rock Vinyl - #.csv', 'a') as Rock:
        writer= csv.writer(Rock, delimiter=',')
        data = [artist,vinyl,checked_date,condition,cat_number,release_date,label,link]
        writer.writerow(data)


if __name__ == "__main__":
    main()
