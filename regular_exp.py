import re

# using re.search() like find()




hand = open('text_files/mbox-short.txt')

# find() version

for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

# re.search() version

hand = open('text_files/mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('From:', line):        # no actual re here, just literal string 'From:' standing in for one.
        print(line)

# using re.search() like startswith()

hand = open('text_files/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

hand = open('text_files/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):       # caret F... means "from beginning of line" 
        print(line)



