import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
name_pattern = r'by_(\w+).html'

name_sequence = []

for i in range(count):  #  how many times we do this entire process

    html = urllib.request.urlopen(url).read()     # retrieve the page
    soup = BeautifulSoup(html, 'html.parser')    # turn it into soup

    print('Retrieving: {}'.format(url))   # print page being retrieved currently

    names_from_page = []    # these will get reset like this, every outer loop
    urls_from_page = []     # thereby only reflecting -current page-

    tags = soup('a')        # get all 'a href' tags from current page
    for tag in tags:        # loop through the tags we retrieved
        name = re.findall(name_pattern, str(tag))[0] # extract name from tag
        url = tag.get('href', None)         # extract url from tag

        names_from_page.append(name)   # build the list in outer loop
        urls_from_page.append(url)

    # find the specific url and name we need from the lists
    # NOTE: make sure this block is outside the inner loop!
    url = urls_from_page[position-1]         # -1 due to zero-based indexing
    target_name = names_from_page[position-1]

    name_sequence.append(target_name)

# print the final retrieved url
print('Retrieving: {}'.format(url)) # otherwise last entry isn't printed
print('Final name in Sequence: {}'.format(name_sequence[-1]))
# alternately, you could just print the target_name variable, since its
# current value will be the last name found






