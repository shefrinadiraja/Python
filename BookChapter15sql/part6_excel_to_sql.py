import pandas 
data = pandas.read_csv('/Users/thahazykandy/Desktop/Python/BookChapter15sql/tracks.csv',header=None)
print(data)
nl = data.values.tolist()
print(nl)


import sqlite3
conn = sqlite3.connect('/Users/thahazykandy/Desktop/Python/BookChapter15sql/music.sqlite')
cur = conn.cursor()
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)

cur.executemany('insert into Tracks (title, plays) values (?,?)',nl)
conn.commit()

conn.close()


