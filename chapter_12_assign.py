import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = 'http://py4e-data.dr-chuck.net/comments_322928.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')

# my original attempt:

# values = []
# for tag in tags:
#     val = re.findall(p, str(tag))[0]  # findall returns a list, so we index it.
#     values.append(int(val))

# print(sum(values))

# then I figured out the listcomp version of the above:

print(sum([int(re.findall(r'\d+', str(tag))[0]) for tag in tags]))





