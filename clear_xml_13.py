import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# extract all the comment/count values from the url and get the sum of all of them
url = 'http://python-data.dr-chuck.net/comments_217218.xml'

# read in the content of the url as a string
data = urllib.request.urlopen(url).read()  # data is a string of the url contents

# I think this only works because the url in question is *already* xml content
# transform the string content into a xml tree
tree = ET.fromstring(data)  # the format of the string is xml....

# find all count elements
counts = tree.findall('comments/comment/count')

# if you look at the actual xml, you will see the nesting used above

# extract the value of each count element and add it to the total
total = 0
for count in counts:
    total += int(count.text)

print('total: ', total)

