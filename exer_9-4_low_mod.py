filename = input('Enter file: ')

handle = open(filename)

my_dict = {}

for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()

    sender = words[1]
    my_dict[sender] = my_dict.get(sender, 0) + 1

lowest = None

for key, val in my_dict.items():
    if lowest == None:
        lowest = val
    else:
        if val < lowest:
            lowest = val
            sender = key

print(sender, lowest)



   




