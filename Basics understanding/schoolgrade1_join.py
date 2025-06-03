import sqlite3
db_connection = sqlite3.Connect('school1.db')
db_cur=db_connection.cursor()
db_cur.execute(''')