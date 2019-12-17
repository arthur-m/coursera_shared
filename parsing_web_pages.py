import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# url = input('Enter URL: ')

url = 'http://data.pr4e.org/page1.htm'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# bs works by feeding it string arguments
# 'a' is anchor tags
# 'html.parser' is the html parser, etc.
# you just have to learn each of them

# Retrieve all of the anchor tags
tags = soup('a')      # creates a list of all anchor tags in the document
for tag in tags:
    print(tag.get('href', None)) # tag is a dict, return value for key 'href'

