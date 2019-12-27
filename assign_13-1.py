import urllib.request, urllib.parse, urllib.error
import json

user_continue = True

counter = 0
running_total = 0

while user_continue:
    url = input('Enter location, or Q to quit: ')
    if url == 'Q' or url == 'q':
        user_continue = False
        continue

    # this should open the webpage and copy the contents;
    # the contents will be a long string, formatted in JSON format
    page_data = urllib.request.urlopen(url).read()

    character_count = len(page_data)
    print('Retrieved {} characters'.format(character_count))
    # in the assignment, it's not clarified what 'characters' are actually
    # supposed to be counted, so I'm simply counting the whole page contents


    # now we convert that String of JSON info into a proper python dict
    comments_dict = json.loads(page_data)

    for d in comments_dict['comments']:
        counter += 1
        running_total += int(d['count'])

    print('Count: {}'.format(counter))
    print('Sum: {}'.format(running_total))


# url_one = 'http://py4e-data.dr-chuck.net/comments_42.json'
# url_two = 'http://py4e-data.dr-chuck.net/comments_322931.json'




