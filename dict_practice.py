# counting values in a list

my_list = ['bill', 'bob', 'bill', 'ted', 'terrence', 'bob', 'bill', 'james', 'ted']

counts = {}

for name in my_list:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1


print(counts)
