import sqlite3
conn = sqlite3.connect('/Users/thahazykandy/Desktop/Python/BookChapter15sql/music.sqlite')
cur = conn.cursor()
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)

new_tacks = [
    ['happy',20],
    ['one day',30],
    ['cool ',20],
    ['second  day',30],
    ['happy',40],
    ['third day',50]
]
cur.executemany('insert into Tracks (title, plays) values (?,?)',new_tacks)
conn.commit()

conn.close()
