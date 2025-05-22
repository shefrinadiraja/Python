import sqlite3
filename = 'movie.db'
db_connection = sqlite3.connect(filename)
db_cur = db_connection.cursor()

msg = "create table if not exists movie (title, rating)"
db_cur.execute(msg)
db_connection.commit()

# msg = "insert into movie (title, rating) values (?, ?)"
#db_cur.execute(msg, (name.strip(), rat.strip()))

inp_fil_nm = "movies.txt"
data = open(inp_fil_nm)
for line in data.readlines():
    name = line.split('-')[0]
    rat = line.split('-')[1]
    msg = f"insert into movie (title, rating) values ('{name}','{rat}')"
    db_cur.execute(msg)
    db_connection.commit()


db_connection.close()