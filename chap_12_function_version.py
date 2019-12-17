import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = input('Enter: ')
count_num = int(input('Enter count: '))
pos = int(input('Enter position: '))


def parseHtml(url, pos):
    html = urllib.request.urlopen(url).read()   # open the current supplied URL
    soup = BeautifulSoup(html, 'html.parser')          # turn it into soup
    tags = soup('a')                    # grab just the a tags from the soup
    i = 0
    for tag in tags:                # loop through the tags, looking for tag
        i += 1                      # stored at given position
        if i == pos:
            return tag.get('href', None)  # return just the url from that tag

current_num = 0
while current_num < count_num:   # loop from zero up to given count number
     print('Retrieving: ', url)   # print which url is being looked at
     url = parseHtml(url, pos)   # call the parse function to get next url
     current_num += 1            # increment count

print('The Last URL of this turn:', url)   # print final result


