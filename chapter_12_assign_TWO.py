import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url_one= 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url_two = 'http://py4e-data.dr-chuck.net/known_by_Kelisse.html'

name_pattern = r'by_(\w+).html'
url = url_two
count = 7
position = 18

tracked_names = []

for i in range(count):
    html = urllib.request.urlopen(url).read()   # open the page
    soup = BeautifulSoup(html, 'html.parser') # make soup of the page


    # you'll just have to do an initial print out for the first page
    # retreived that is separate from the for tag loop

    # the problem is, if you print that in here, it will happen on
    # every pass of THIS for loop, for i in range().

    # is there info that can be shifted to this space that is printed
    # in here succesively on loops of 'for i in range' and -different-
    # info that is only available from the tags that is printed
    # in the tags loop?

    # or can you just shift all the actual printing into THIS space,
    # which will include the initial findings, but also print out
    # all subsequent findings, even though those subsequent findings
    # are getting -updated- (but not printed) inside the tags loop.
    # inner tags loop: update values
    # outer range loop: print results

    tags = soup('a') # get the tags from the soup we made

    names = [] # for -each site- we need all the names on it
    urls = []  # and for -each site- we need all the addresses on it

                # because we are then going to find the ONE name + address
                # that we visit next, and so on.

    for tag in tags:    # we need to loop through the tags of current page
        name = re.findall(name_pattern, str(tag))[0]
        address = tag.get('href', None) # treat tags like dictionaries
                                        # get the value for key 'href'
        names.append(name)
        urls.append(address)

    #print(names[position-1]) # get just the name we want, based on val of position
    #print(urls[position-1]) # get just the address we want, also based on val of position

    tracked_names.append(names[position-1])

    url = urls[position-1]   # this is essential, as it updates url for the next pass

print(tracked_names[-1])

