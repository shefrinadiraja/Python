import sqlite3
conn = sqlite3.connect('/Users/thahazykandy/Desktop/Python/BookChapter15sql/music.sqlite')
cur = conn.cursor()




cur.execute('UPDATE Tracks set plays=90 where title="Thunderstruck"')
conn.commit()

cur.execute('UPDATE Tracks set plays=? where title=?',(299,'Thunderstruck'))
conn.commit()



cur.close()