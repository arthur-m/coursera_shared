import sqlite3

# The data model creates the features of the application;
# What is in the data model determines what the application is capable of doing.

 # is the column an object itself, or an attribute of another object?
 # once we define objects, we need to define relationships between objects.

# Table 1: Track - Object
# title, song length, play count, rating - Attributes of Track Object

# where you find replicated data, you know it's not 'part of the track object',
# but rather its own thing that is related to track object.
# Band name, album name, genre* -- new objects with a relationship to the
# Track object.

# however, genre, though it is repeated data, is tied to track (updating
# genre only changes tag for a track, not for an artist or album)

# Table
# Primary Key   -   each row has one, used to point to that row by others (Foreign Keys)
# Logical Key   -   optional, a unique thing that might be used to find row from outside world
# Foreign Key   -   in 'other' row, points to a primary key of diff row

# logical key example: if table 'Track' has title, rating, len, count, 'title'
# is a good logical key because you'd likely look up a song by its title, whereas
# you are not likely to look it up (specifically) by it's rating, length, or
# playcount.
