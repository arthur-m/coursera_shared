import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
#url = input('Enter URL: ')

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retreiving {}'.format(url))

xml = urllib.request.urlopen(url).read()
print('Retrieved: {} characters'.format(str(len(xml))))

root = ET.fromstring(xml)


# can also retrieve count without the shorthand:
# count s= root.findall('comments/comment/count')
counts = root.findall('.//count')
print('Count: {}'.format(str(len(counts))))

x = 0
for count in counts:
    x += int(count.text) # retrieve text from count tag & make it an int

print('Sum: {}'.format(str(x)))   # need to make total a string to print it

# actually, the point of format is that it will handle the conversion itself:

print('Sum: {}'.format(x))  # no need to convert x to string when using format()
