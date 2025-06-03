import sqlite3
db_connection = sqlite3.connect('school1.db')
db_cur = db_connection.cursor()

db_cur.execute('DROP table if exists grades')

make_tablecommand_student =('''create table if not exists students (student_id integer primary key autoincrement,
                            first_name TEXT,
                            second_name TEXT)''')
db_cur.execute(make_tablecommand_student)

make_tablecommand_grade=('''create table if not exists grades (grade_id integer primary key autoincrement,
                         student_id integer,
                         subject TEXT,
                         grade INTEGER)''')
db_cur.execute(make_tablecommand_grade)
students=[
         ('Eisa','Zain'),
         ('Eid','Zain'),
         ('Adam','Zain')
]
db_cur.executemany('''insert into students(first_name,second_name) values (?,?)''',(students))
db_connection.commit()
db_cur.execute("select student_id from students")
student_ids =[row[0] for row in db_cur.fetchall()]
grades=[
    (student_ids[0], 'Math', 'A'),
    (student_ids[0], 'Science','A'),
    (student_ids[0], 'English', 'A'),

    (student_ids[1], 'Math','B'),
    (student_ids[1], 'Science','A'),
    (student_ids[1], 'English','B'),

    (student_ids[2], 'Math','A'),
    (student_ids[2], 'Science','A'),
    (student_ids[2], 'English','B')
]
db_cur.executemany('''insert or ignore into grades(student_id,subject,grade) values (?,?,?)''', grades)
db_connection.commit()
db_connection.close()
print('Data inserted sucessfully')

