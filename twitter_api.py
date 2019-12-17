import urllib.request, urllib.parse, urllib.error
import twurl    # chuck wrote this apparently ?
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    prnt('')
    acct = input('Enter Twitter Account: ')
    if (len(acct) < 1):
        break

    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})

    print('Retreiving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode() # returns string representation of JSON data
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent=4))

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print(' ', s[:50])


