filename = 'text_files/romeo.txt'

handle = open(filename)

counts = {}

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

l = []
for key, val in counts.items():
    newtup = (val, key)
    l.append(newtup)


# we can rewrite the above four lines of code in one line via use of a listcomp:

l = sorted([(val, key) for key, val in counts.items()], reverse=True)       # same as lines 12-15 above

#l = sorted(l, reverse=True)    # reverse will make it sort High to Low
                                # this use of sorted() didn't need to be a separate line; look how I added
                                # it to the list comp above instead.

for key, val in l[:10]:
    print(val, key)          # because we flipped them around in the list comp, to sort by the values, not the keys


# the point of all of this is to show sorting of dictionaries contents by the VALUES rather than by the keys
# we create 'l', a list of tuples, in which the key-value pairs from the original dictionary 'counts' have been flipped,
# so that we can then sort via the "keys" which are actually the values from the original.


