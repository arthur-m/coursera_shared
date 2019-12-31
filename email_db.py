import sqlite3

conn = sqlite3.connect('emaildb.sqlite') # name of created database
cur = conn.cursor() # create a cursor to send commands / receive responses through

cur.execute('DROP TABLE IF EXISTS Counts') # does nothing if db above was
# just created; if it already exists, this will drop the existing 'Counts' table in it.

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    # use placeholder '?' to refer to variables rather than writing
    # variables into the SQL statements themselves (dangerous)
    # next line accesses DB, -not- the file we are grabbing data from.
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) # (email,) is a tuple with one item in it.
    row = cur.fetchone() # the above line can be thought of as 'open the data'; this actually grabs it.
    if row is None: # email not found in db, so add it:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    # email found in db, so update it.
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

# always distinguish clearly in mind between data source (in this case mbox-short.txt)
# and the database we are building.
