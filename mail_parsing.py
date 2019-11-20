filename = 'text_files/mbox-short.txt'

fo = open(filename)

count = 0
for line in fo:
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        print(words[1])
        count += 1

print('There were {} lines in the file with From as the first word'.format(count))



# accomplishes same task as above, just different approach; wastefully strips and splits all lines, however.

for line in fo:
    line = line.rstrip()
    words = line.split()

    if len(words) < 1 or words[0] != 'From':
        continue

    else:
        print(words[1])
        count += 1

print('There were {} lines in the file with From as the first word'.format(count))
