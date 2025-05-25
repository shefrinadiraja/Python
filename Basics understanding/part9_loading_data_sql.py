import json
import sqlite3

db_connection = sqlite3.connect('social.db')
db_cur = db_connection.cursor()


command='''select images.id, images.description, users.firstname, users.lastname 
from images,users
where images.user_id = users.id'''
db_cur.execute(command)
data = db_cur.fetchall()
print(data)