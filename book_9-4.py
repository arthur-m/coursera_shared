# fname = input('Enter File: ')
# if len(fname) < 1: fname = 'mbox-short.txt'
# hand = open(fname)

filename = 'text_files/clown.txt'
handle = open(filename)


# this is just a non-get() version of this sort of 'counting' pattern

di = {}
for line in handle:
    line = line.rstrip()
    words = line.split()

    for word in words:
        if word in di:
            di[word] = di[word] + 1 # remember, this assigns an INT VALUE to the key 'word' in dictionary 'di'.
            #print('**Existing**')
        else:
            di[word] = 1
            #print('**NEW**')

        #print(word, di[word])


print(di)


# version with get()

handle = open(filename)     # handle is interesting here: if we don't re-open the file and assign it to handle again 
                            # the above work, handle will have no contents. is this because it works like an iterator /
                            # generator object and picks up where it left off? (probably!)

di = {}

for line in handle:
    words = line.split()

    for word in words:
        di[word] = di.get(word, 0) + 1

print(di)

# you can use get() in other contexts besides the 'create or modify key' scenario you've been doing.