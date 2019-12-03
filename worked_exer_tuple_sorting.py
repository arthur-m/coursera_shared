filename = 'text_files/clown.txt'

handle = open(filename)

di = {}

for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        di[word] = di.get(word, 0) + 1

x = sorted(di.items())      # sorted by key
print(x[:5])                # print just the first 5

# but that sorted the keys, which are the words. 
# we want to sort by the counts.

l = [(v, k) for k, v in di.items()]

for v, k in sorted(l[:5], reverse=True):       # sorted() is called on our list l, from High to Low (reversed=True)
    print(k, v)                           # l is a list of tuples. the *first values* in the tuples will be compared.
                                           # because we swapped the values for the keys when we built l, those first
                                           # items in the tuples will be the values from the dictionary (the counts)
                                          # so, we are thereby sorting the counts, not the words.

                                           # NOTE: when we print them out, we reverse the order: print(k, v)
                                           # simply so that the printout shows the word first, count second

                                           # you could also do this by flipping the v, k in the for loop to k, v
                                           # and not swapping in the print statement
                                           # (point being you just need to swap them once, somewhere)

                                           # BUT REMEMBER! the names v, k or k, v in the for loop are just arbitrary
                                           # names you're assigning to the values in the list of tuples. as long as
                                           # you track what values they refer to, you can choose to print them out
                                           # in whatever order you desire.


# NOTE:   the loop above is interesting, because it has TWO VARIABLES but is on ONE ITEM, 'l'

# the reason it works is because 'l' contains tuples, and Python is smart, and knows that the two variables
# should correspond to the *two values held in each tuple in the list (l)*

# this is just another example of the tuple behavior you recently read about in the 'Powerful Python' book, 
# where Python can unpack tuples smartly and as needed (as seen above).

# the [:5] on l is so we just print the first five