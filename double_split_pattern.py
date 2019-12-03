import re

t = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# using find() and slicing

atpos = t.find('@')              # returns index, which is 21

spos = t.find(' ', atpos)        # find a space, *starting from atpos*
                                    # returns index 31

host = t[atpos+1:spos]         # +1 because 21 is the index of the '@' we did find() on, and we
                                    # want to start at the index immediately after the @
                                # up to but not including spos

print(host)

# double split pattern

words = t.split()
email = words[1]
pieces = email.split('@')

end_result = pieces[1]
print(end_result)


# regular expression to do the exact same thing (most elegant version...)

pattern = r'@([^ ]*)'           # [^ ] matches anything that is NOT a whitespace char
                                # [ ] to create the set, ^ inside to say 'not this', character is whitespace.
                                # [^ ]* reads as: a single non-blank character, zero or more times.

y = re.findall(pattern, t)
print(y)


# more detailed, locationally:

p = r'^From .*@([^ ]*)'

x = re.findall(p, t)
print(x)
