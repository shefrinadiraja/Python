import sqlite3
conn = sqlite3.connect('/Users/thahazykandy/Desktop/Python/BookChapter15sql/music.sqlite')
cur = conn.cursor()
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
('My Way', 115))
conn.commit()
print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)




cur.close()