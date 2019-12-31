# my original version that removes the '.com' from the org name,
# which might be why the coursera grader doesn't like my database...

import sqlite3
import re

conn = sqlite3.connect('emaildb_two.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

filename = 'text_files/mbox.txt'
if (len(filename) < 1): filename = 'mbox.txt'

p = re.compile(r'@([\w]*).')      # careful with () and grouping behavior

handle = open(filename)
for line in handle:
    if not line.startswith('From: '):
        continue
    chunks = line.split()
    email = chunks[1]
    org = p.findall(email)[0]  #findall returns a list

    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if not row:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
            (org,))

conn.commit()       # this needs to be outside the loop to speed things up

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr): # row is a list, but what object does execute() return here?
    print(str(row[0]), row[1])  # why do we need str() to print org? what is it?

cur.close()


