# urllib is a library that doe all the socket work for us and
# makes web pages look like a file.

# the idea here is that the socket .connect, .send, .recv methods
# are no longer necessary when using urllib

# that means: this program is a direct replacement of the program
# in 'exercise_req_response.py' and 'network_one.py'
# (it doesn't, however, print the headers by default)

import urllib.request, urllib.parse, urllib.error

fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhandle:
    print(line.decode().strip())

# each line in the file is still a byte array, so we decode() them.
# decode() returns a string

fhandle_two = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts_dict = {}

for line in fhandle_two:
    words = line.decode().split()
    for word in words:
        counts_dict[word] = counts_dict.get(word, 0) + 1
print(counts_dict)


