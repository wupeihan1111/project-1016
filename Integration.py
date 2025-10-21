import tkinter as tk
import sqlite3

root = tk.Tk()
root.title('INTEGRATION')
root.geometry('300x350')

label_id = tk.Label(root, text='Student ID')
label_id.pack(pady=(15,5))
entry_id = tk.Entry(root, width=25)
entry_id.pack()

label_name = tk.Label(root, text='Student Name')
label_name.pack(pady=(10,5))
entry_name = tk.Entry(root, width=25)
entry_name.pack()

def print_student():
    student_id = entry_id.get()
    student_name = entry_name.get()

    print('Student ID:  {}'.format(student_id))
    print('Student Name: {}'.format(student_name))
    print('-'*30)

botton_print = tk.Button(root, text='Print',command=print_student)
botton_print.pack(pady=15)

conn = sqlite3.connect('Student.db')
cursor = conn.cursor()

def create_student():
    student_id = entry_id.get()
    student_name = entry_name.get().lower()

    cursor.execute('INSERT INTO DB_student(db_student_id,db_student_name) VALUES(?,?)', (student_id, student_name))
    conn.commit()

    print('Student ID: {}'.format(student_id))
    print('Student Name: {}'.format(student_name))
    print('-' * 30)

button_create = tk.Button(root, text='Create', command=create_student)
button_create.pack(pady=20)

def overview_student():
    cursor.execute('SELECT * from DB_student')
    overview = cursor.fetchall()
    print(overview)

botton_overview = tk.Button(root, text='Overview', command=overview_student)
botton_overview.pack(pady=25)

root.mainloop()