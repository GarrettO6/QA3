import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

COURSE_CATEGORIES = {
    "International Marketing": "international_marketing",
    "Business Application Development": "business_app_dev",
    "Business Database Management": "business_db_mgmt",
    "Prog Logic and Analytic Thinking": "prog_logic_analytic_thinking",
    "Introduction to Managerial Finance": "intro_managerial_finance"
}

def open_add_question():
    window = tk.Tk()
    window.title("Add New Question")
    window.geometry("500x500")

    tk.Label(window, text="Select Course Category").pack()
    category_var = tk.StringVar()
    category_dropdown = ttk.Combobox(window, textvariable=category_var, values=list(COURSE_CATEGORIES.keys()), state='readonly')
    category_dropdown.pack(pady=5)

    entries = {}
    labels = ["Question", "Option A", "Option B", "Option C", "Option D", "Correct Option (A/B/C/D)"]
    for label in labels:
        tk.Label(window, text=label).pack()
        entry = tk.Entry(window, width=60)
        entry.pack(pady=2)
        entries[label] = entry

    def submit():
        category = COURSE_CATEGORIES.get(category_var.get())
        values = [entries[label].get().strip() for label in labels]

        if not category or not all(values):
            messagebox.showerror("Error", "All fields are required.")
            return

        conn = sqlite3.connect("database/quiz_bowl.db")
        cursor = conn.cursor()
        cursor.execute(f"""
            INSERT INTO {category} (question, option_a, option_b, option_c, option_d, correct_option)
            VALUES (?, ?, ?, ?, ?, ?)
        """, values)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Question added successfully!")
        for entry in entries.values():
            entry.delete(0, tk.END)

    tk.Button(window, text="Submit", command=submit).pack(pady=10)
    tk.Button(window, text="Back", command=window.destroy).pack()

    window.mainloop()
