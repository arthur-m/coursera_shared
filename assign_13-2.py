# my final version. it works.
# it needed the key provided in the call, see the dict with
# address and key.
# if the api_url endpoint is 'geojson?', this key isn't necessary.
# no idea why, but that's what I learned trying to do this.
# also note that .decode() isn't necessary after .read() when getting
# the data from the handle, uh. I don't know why, because in geojson.py
# chuck does .read().decode() to get the data.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_url = 'http://py4e-data.dr-chuck.net/json?'

loc = input('Enter location: ')
url = api_url + urllib.parse.urlencode({'address': loc, 'key': 42})

print('Retrieving {}'.format(url))

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()            # if you add .decode() it still works.. why?

info = json.loads(data)
print('Retrieved {} characters'.format(len(data)))


#print(json.dumps(info, indent=4))

place_id = info['results'][0]['place_id']

print('Place id {}'.format(place_id))

