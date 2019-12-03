# counting values in a list

my_list = ['bill', 'bob', 'bill', 'ted', 'terrence', 'bob', 'bill', 'james', 'ted']

counts = {}

for name in my_list:
    if name not in counts:
        counts[name] = 1            # add new entry and set it to value 1
    else:
        counts[name] += 1           # add 1 to the existing value

print(counts)

# get() exists to help us check for a key in a dictionary, avoiding traceback if that key doesn't exist.

x = counts.get('zebulon', 'not found')  # get() returns value for provided key, or 2nd arg (default) if key not found
print(x)

# siplified counting pattern using get()
# get makes the entire if - else statement in the above version condensed to one line of code!

counts_two = {}
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:
    counts_two[name] = counts_two.get(name, 0) + 1      # this one line either modifies OR creates an entry in dict
    

print(counts_two)






