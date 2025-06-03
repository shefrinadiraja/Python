import streamlit as st
import sqlite3


conn = sqlite3.connect('school3.db')
curr = conn.cursor()

curr.execute('DROP TABLE IF EXISTS students')
curr.execute('DROP TABLE IF EXISTS fee_status')


curr.execute('''CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT)''')
curr.execute('''CREATE TABLE IF NOT EXISTS fee_status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                fee_paid BOOLEAN,
                FOREIGN KEY (student_id) REFERENCES students(id))''')


# option to add students streamlit app
st.title("Student Fee Management System")
def add_student(first_name, last_name):
    curr.execute('INSERT INTO students (first_name, last_name) VALUES (?, ?)', (first_name, last_name))
    conn.commit()
    st.success(f"Student {first_name} {last_name} added successfully!")
def add_fee_status(student_id, fee_paid):
    curr.execute('INSERT INTO fee_status (student_id, fee_paid) VALUES (?, ?)', (student_id, fee_paid))
    conn.commit()
    st.success(f"Fee status for student ID {student_id} updated successfully!")
    
st.subheader("Add Student")
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
if st.button("Add Student"):
    if first_name and last_name:
        add_student(first_name, last_name)
    else:
        st.error("Please enter both first and last names.")
st.subheader("Update Fee Status")
student_id = st.number_input("Student ID", min_value=1, step=1)
fee_paid = st.checkbox("Fee Paid")

if st.button("Update Fee Status"):
    if student_id:
        add_fee_status(student_id, fee_paid)
    else:
        st.error("Please enter a valid student ID.")

# Display all students and their fee status
st.subheader("Student List and Fee Status")
curr.execute('''SELECT s.id, s.first_name, s.last_name, f.fee_paid
               FROM students s LEFT JOIN fee_status f ON s.id = f.student_id''')

students = curr.fetchall()
if students:
    for student in students:
        student_id, first_name, last_name, fee_paid = student
        fee_status = "Paid" if fee_paid else "Not Paid"
        st.write(f"ID: {student_id}, Name: {first_name} {last_name}, Fee Status: {fee_status}")
else:
    st.write("No students found.")





