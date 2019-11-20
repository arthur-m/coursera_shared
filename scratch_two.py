# filename = input('Enter name of file: ')

# file_handle = open(filename)

# count = 0
# running_total = 0.0

# for line in file_handle:
#     if not line.startswith('X-DSPAM-Confidence'):   # we only want lines that start this way, so continue past all that don't.
#         continue
#     else:
#         val_index = line.find(':')
#         running_total += float(line[val_index+1:].strip())
#         count += 1

# print('Averge spam confidence: {}'.format(running_total/count))



filename = 'text_files/mbox-short.txt'

fh = open(filename)

count = 0
running_total = 0

for line in fh:
    if not line.startswith('X-DSPAM-Confidence'):
        continue
    else:
        index = line.find(' ')
        value = float(line[index:].strip())
        running_total += value
        count += 1

average  = round(running_total/count, 12)     


print('Average spam confidence: {}'.format(average))


# round() -- two arguments: value to round, number of decimal places to round to.

