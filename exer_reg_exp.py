
# my first attempt...
# import re

# filename = 'regex_sum_322926.txt'
# handle = open(filename)

# pattern = r'[0-9]+'
# all_nums = []

# for line in handle:
#     found_nums = re.findall(pattern, line)     # findall returns a list of ints (as strings) found on the current lines
#     if found_nums:
#         for num in found_nums:
#             all_nums.append(int(num))

# the_sum = sum(all_nums)
# print(the_sum)


# trying to do it without the redundancy of the findall list and my own list, all_nums...
# actually, your logic makes sense: create one master list that holds everything found, because each pass of the for
# loop will return (via findall) one list representing just on line of the file. that list can't be the master list, it's
# just one line, so I aggregrate the results into the all_nums list.

import re

filename = 'regex_sum_322926.txt'
p = r'[0-9]+'
all_nums = []

handle = open(filename)
for line in handle:
    found_nums = [int(x) for x in re.findall(p, line)]
    all_nums.extend(found_nums)

print(sum(all_nums))


# then I figured out the much cleaner list comprehension version...

# import re
# print(sum([int(x) for x in re.findall('[0-9]+', open('regex_sum_322926.txt').read())]))



import re
print(sum([int(x) for x in re.findall('[0-9]+', open('filename').read())]))

# NOTE: the above listcomp does NOT go line-by-line through the file; it's totally different than the previous approaches.
# it uses .read() instead of a for loop (which would go line by line); read() on the other hand will, by default, return 
# the *entire file*. There is a for loop in this listcomp of course, but it's not reading the file line by line; it's
# going through the entire contents of the re objet returned by findall(), which contains all pattern matches, and one by 
# one changing the match into an int, and then packing it into a list -- because that's what a listcomp does, is build a 
# list.

# .read() returns the entire contents of the file in one big string
# findall() looks at that string and finds all the matches to the re pattern, and returns an list with those matches
# the for loop goes through that list and turns each one into an int, and packs it into
# a list, which we then call sum() and print() on.


                                    

