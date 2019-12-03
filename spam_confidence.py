import re

hand = open('text_files/mbox-short.txt')

numlist = []

for line in hand:
    line = line.rstrip()
    pattern = r'^X-DSPAM-Confidence: ([0-9.]+)'     # NOTE: the period here . is a literal period, not a regex command
                                                    # it doesn't need an escape char because it's inside brackets;
                                                    # stuff inside brackets is always read as "match a single character
                                                    # to anything in this set". But, the + after the brackets says, 
                                                    # one or more of the bracket / set character.

    stuff = re.findall(pattern, line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])       # it's a string, so make it a float
    numlist.append(num)

print('Maximum:', max(numlist))



