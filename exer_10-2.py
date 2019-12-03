filename = 'text_files/mbox-short.txt'

handle = open(filename)

d = {}

for line in handle:
    if not line.startswith('From '):
        continue

    line = line.rstrip()
    words = line.split()        # split() returns a list of each word in the line, whitespace divider

    timestamp = words[5]        # index 5 of the words list is the timestamp 
    hour = timestamp[:2]        # now we just slice the timestamp to grab the first two digits of timestamp
                                # (we didn't need to split the string again at the ':', this is easier)

    d[hour] = d.get(hour, 0) + 1 # build up the dictionary with a count of the hours using the get() method

# we want to sort the hours. we don't need the fancy temp listcomp k, v swap - that is for sorting VALUES. 
# sorting a dictionary is by default a sort of the KEYS
# 'hours' is already our key. if you do the listcomp flip, you'd have the 'counts' as the keys.


for key, val in sorted(d.items()):    # sorts the key, value pairs of dictionary 'd' by key (default)
    print(key, val)







