import json
import sqlite3

db_connection = sqlite3.connect('books.db')
db_cur = db_connection.cursor()

make_table_coomand = '''Create table if not exists books 
(id integer primary key, title text, author TEXT,genre TEXT, rating Real )'''
command_insert_data = '''
insert into books ( title, author ,genre , rating ) values (?,?,?,?)
'''


db_cur.execute(make_table_coomand)


# file = open('book.json')
# data=json.load(file)



def add_details(a,b,c,d):
    db_cur.execute(command_insert_data,[a,b,c,d])
    db_connection.commit()

# for d in data:
#     t,a,g,r = d ['title'] , d['author'], d['genre'], d['rating']
#     add_details(t,a,g,r)



add_details("harry's pottr","noah's apple",'comdey','5.0')

add_details('a','dsa','mango',6)




db_connection.close()



