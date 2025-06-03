import sqlite3
conn = sqlite3.connect('/Users/thahazykandy/Desktop/Python/BookChapter15sql/music.sqlite')
cur = conn.cursor()
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)
cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()



cur.close()