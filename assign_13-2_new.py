# version to contrast with original assign_13-2.py

import urllib.request, urllib.parse, urllib.error
import json

service_url = 'http://py4e-data.dr-chuck.net/geojson?'

loc = input('Enter location: ')
url = service_url + urllib.parse.urlencode({'address': loc})

print('Retrieving {}'.format(url))

uh = urllib.request.urlopen(url)

data = uh.read()        # no decode, why? geojson uses decode here as well.
info = json.loads(data)
print('Retrieved {} characters'.format(len(data)))

place_id = info['results'][0]['place_id']

print('Place id: {}'.format(place_id))

