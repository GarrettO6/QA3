import tkinter as tk
from tkinter import ttk
import sqlite3

from add_question import COURSE_CATEGORIES

def open_view_questions():
    window = tk.Tk()
    window.title("View Questions")
    window.geometry("800x400")

    tk.Label(window, text="Select Course Category").pack()
    category_var = tk.StringVar()
    category_dropdown = ttk.Combobox(window, textvariable=category_var, values=list(COURSE_CATEGORIES.keys()), state='readonly')
    category_dropdown.pack(pady=5)

    text_area = tk.Text(window, wrap="word", width=100, height=20)
    text_area.pack(pady=10)

    def load_questions():
        table = COURSE_CATEGORIES.get(category_var.get())
        if not table:
            return
        conn = sqlite3.connect("database/quiz_bowl.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, question FROM {table}")
        records = cursor.fetchall()
        conn.close()

        text_area.delete("1.0", tk.END)
        for row in records:
            text_area.insert(tk.END, f"ID {row[0]}: {row[1]}\n\n")

    tk.Button(window, text="Load Questions", command=load_questions).pack()
    tk.Button(window, text="Back", command=window.destroy).pack(pady=10)

    window.mainloop()
