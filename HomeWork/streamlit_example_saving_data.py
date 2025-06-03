import streamlit as st
import sqlite3

# Initialize database only once
def init_db():
    conn = sqlite3.connect('school2.db')
    cur = conn.cursor()

    cur.execute('DROP table if exists grades')
    cur.execute('DROP table if exists students')

    cur.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    second_name TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS grades (
                    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    subject TEXT,
                    grade TEXT,
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
    cur.executemany('INSERT INTO students(first_name, second_name) VALUES (?, ?)', students)
    conn.commit()

    cur.execute('SELECT id, first_name FROM students')
    student_dict = {name: sid for sid, name in cur.fetchall()}

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

    cur.executemany('INSERT OR IGNORE INTO grades(student_id, subject, grade) VALUES (?, ?, ?)', grades)
    conn.commit()
    conn.close()

@st.cache_resource
def get_connection():
    return sqlite3.connect("school2.db", check_same_thread=False)

def get_students():
    cur = conn.cursor()
    cur.execute("SELECT id, first_name, second_name FROM students")
    return cur.fetchall()

def get_grades(student_id):
    cur = conn.cursor()
    cur.execute("SELECT subject, grade FROM grades WHERE student_id = ?", (student_id,))
    return cur.fetchall()

def add_student(first_name, second_name):
    cur = conn.cursor()
    cur.execute("INSERT INTO students(first_name, second_name) VALUES (?, ?)", (first_name, second_name))
    conn.commit()

def add_grade(student_id, subject, grade):
    cur = conn.cursor()
    cur.execute("INSERT INTO grades(student_id, subject, grade) VALUES (?, ?, ?)", (student_id, subject, grade))
    conn.commit()

# --- Streamlit UI ---
st.title("🎓 Student Grades Manager")

# One-time setup (drop + insert sample data)
if st.button("🔁 Reset and Load Sample Data"):
    init_db()
    st.success("Database reset and sample data inserted!")

conn = get_connection()

# Add Student
st.subheader("➕ Add New Student")
with st.form("add_student_form"):
    first = st.text_input("First Name")
    last = st.text_input("Second Name")
    submitted = st.form_submit_button("Add Student")
    if submitted:
        add_student(first, last)
        st.success(f"Added student: {first} {last}")

# Add Grade
st.subheader("📘 Add Grade")
students = get_students()
student_names = {f"{first} {last}": sid for sid, first, last in students}
selected_name = st.selectbox("Select Student", list(student_names.keys()))
subject = st.text_input("Subject")
grade = st.selectbox("Grade", ['A', 'B', 'C', 'D', 'F'])
if st.button("Add Grade"):
    add_grade(student_names[selected_name], subject, grade)
    st.success(f"Added grade {grade} in {subject} for {selected_name}")

# Display Students and Grades
st.subheader("📋 All Students and Grades")
for sid, first, last in students:
    st.markdown(f"**{first} {last}**")
    grades = get_grades(sid)
    for subject, grade in grades:
        st.markdown(f"- {subject}: {grade}")
