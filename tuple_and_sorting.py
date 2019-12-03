d = {'a': 10, 'c': 22, 'b': 1}

x = d.items()

print(x)
print(type(x))

# items returns a tuple for each key-value pair, inside a list (though the type is actually 'dict_items'):

# [('a', 10), ('c', 22), ('b', 1)]      # this is the 'list' of tuples, where a tuple is key: value pair from dict d

y = sorted(x)       # it sorts by comparing the first items in the tuples: so it sorts the a,c,b to a,b,c
print(y)            # if the keys were all the same, it would move on to comparing the values


# naturally we can't do .sort() on tuples, because they are immutable.




# much faster version, no need for intermediary variables (x in the above):

d = {'a': 10, 'c': 22, 'b': 1}
t = sorted(d.items())
print(t)

# because of all this,
# we can loop through a sorted version of the dictionary -- sorting by keys:

for k, v in sorted(d.items()):      # the dictionary has been sorted becaused sorted works on the keys
    print(k, v)




# sorting by values in a dictionary instead of keys requires some trickery, it seems:

lc = [(v, k) for k, v in d.items()]
# print(lc)

lc = sorted(lc, reverse=True)
print(lc)


# k, v for d.items() works because .items() returns a tuple of two values (key value pairs, specifically)
# so the assignment of k, v (two variables) to a tuple with two values makes sense

