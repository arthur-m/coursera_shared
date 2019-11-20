album_data = {
    'Harm\'s Way': {
        'Money Made': 999.973,
        'Year of Release': 2010,
        'Formats': ['digital', 'CD']
    },
    'Eyes On Backwards': {
        'Money Made': 10459.929,
        'Year of Release': 2016,
        'Formats': ['digital', 'CD', 'Vinyl']
    }
}

album_one = album_data['Eyes On Backwards']

album_one['Ranking'] = 10

print(album_one['Ranking'])

print(album_data['Eyes On Backwards'].keys())

x = album_one is album_data['Eyes On Backwards']

print(x)


# ok, so you are actually modifying the dictionary stored in album_data even though you've assigned it to a 
# new variable.

# so, how to make a copy....

album_two = album_data['Harm\'s Way'].copy()

print(album_two)



# there's this question of: 
# is the 'name' of the data object a thing stored in the data object itself, e.gl: key = 'Name', value = 'Harm's Way'
# or is the 'name' of the data object the actual variable name, e.g.  harms_way = {}

# it's important to distinguish between these two things, they are quite different:
# a piece of data, a value, that is provides the name for that data set, as implemented by the programmer: 
# e.g. a key that = album name, like in my dictionary album_data
# vs. a variable name (quite literally, a 'name') such as album_one = {}

# the problem with the latter case is that once you package that variable in a container, it loses its name
# albums = []
# albums.append(album_one)
# album_one's data is now stored in the list albums, but the name it had, album_one, isn't utilized anywhere inside
# that list. python still has the data assigned to the name album_one, it's still accessible that way, but insofar as it
# exists insid the list albums, it's now just albums[-1] (for now) and inside the list it doesn't have the name
# 'album_one'.





