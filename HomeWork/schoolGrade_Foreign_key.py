import sqlite3
db_connection = sqlite3.connect('school2.db')
db_cur = db_connection.cursor()


db_cur.execute('DROP table if exists grades')
db_cur.execute('DROP table if exists students')



db_cur.execute('''create table if not exists students (
                            id integer primary key autoincrement,
                            first_name TEXT,
                            second_name TEXT)''')
db_cur.execute('''create table if not exists grades (
                            grade_id integer primary key autoincrement,
                            student_id integer,
                            subject TEXT,
                            grade INTEGER,
                            FOREIGN KEY (student_id) REFERENCES students(id))''')

students = [
    ('Eisa', 'Zain'),
    ('Eid', 'Zain'),
    ('Adam', 'Zain'),
    ('Sara', 'Khan'),
    ('Ali', 'Ahmed'),
    ('Fatima', 'Ali'),
    ('Omar', 'Hassan'),
    ('Laila', 'Yusuf'),
    ('Zara', 'Khan'),
    ('Bilal', 'Ahmed')
]
db_cur.executemany('''insert into students(first_name, second_name) values (?, ?)''', students)
db_connection.commit()

db_cur.execute('SELECT student_id, first_name FROM students')
student_dict = {name: sid for sid, name in db_cur.fetchall()}

grades = [
    (student_dict['Eisa'], 'Math', 'A'),
    (student_dict['Eisa'], 'Science', 'A'),
    (student_dict['Eisa'], 'English', 'A'),

    (student_dict['Eid'], 'Math', 'B'),
    (student_dict['Eid'], 'Science', 'A'),
    (student_dict['Eid'], 'English', 'B'),

    (student_dict['Adam'], 'Math', 'A'),
    (student_dict['Adam'], 'Science', 'A'),
    (student_dict['Adam'], 'English', 'B')
]

db_cur.executemany('''insert or ignore into grades(student_id, subject, grade) values (?, ?, ?)''', grades)

db_connection.commit()
db_connection.close()



