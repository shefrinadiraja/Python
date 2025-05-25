import json
import sqlite3

db_connection = sqlite3.connect('social.db')
db_cur = db_connection.cursor()

make_table_coomand1 = ''' 
create table if not exists users (
id int primary key,
firstname TEXT,lastname TEXT
)
'''
db_cur.execute(make_table_coomand1)
db_connection.commit()

make_table_command2='''
create table if not exists images (
id int primary key,
user_id INT,
description TEXT,
foreign key (user_id) references users(id)
)
'''
db_cur.execute(make_table_command2)
db_connection.commit()
user_data = [
    (1,'umair','ali'),
    (2,'shefrin','adiraja'),
    (3,'eisa','zain'),
    (4,'eid','zain')
]

db_cur.executemany("insert into users (id,firstname,lastname) values (?,?,?)" , user_data)

db_connection.commit()

image_data= [
    (1,2,'good'),
    (2,3,'great picture'),
    (3,2,'nice')
]
db_cur.executemany("insert into images (id,user_id,description) values (?,?,?)", image_data)
db_connection.commit()