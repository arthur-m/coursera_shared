import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input('Enter URL: ')

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retreiving {}'.format(url))

xml = urllib.request.urlopen(url).read()
print('Retrieved: {} characters'.format(str(len(xml))))

root = ET.fromstring(xml)

counts = root.findall('.//count')
print('Count: {}'.format(str(len(counts))))

x = 0
for count in counts:
    x += int(count.text)

print('Sum: {}'.format(str(x)))

