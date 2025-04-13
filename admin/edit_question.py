import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from add_question import COURSE_CATEGORIES

def open_edit_question():
    window = tk.Tk()
    window.title("Edit/Delete Questions")
    window.geometry("850x650")

    tk.Label(window, text="Select Course Category").pack()
    category_var = tk.StringVar()
    dropdown = ttk.Combobox(window, textvariable=category_var, values=list(COURSE_CATEGORIES.keys()), state='readonly')
    dropdown.pack(pady=5)

    question_listbox = tk.Listbox(window, width=100)
    question_listbox.pack(pady=10)

    selected_id = None
    current_table = None

    form_entries = {}
    form_labels = ["Question", "Option A", "Option B", "Option C", "Option D", "Correct Option (A/B/C/D)"]

    for label in form_labels:
        tk.Label(window, text=label).pack()
        entry = tk.Entry(window, width=80)
        entry.pack(pady=2)
        form_entries[label] = entry

    def load_questions():
        nonlocal current_table
        current_table = COURSE_CATEGORIES.get(category_var.get())
        if not current_table:
            return

        question_listbox.delete(0, tk.END)

        conn = sqlite3.connect("database/quiz_bowl.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, question FROM {current_table}")
        records = cursor.fetchall()
        conn.close()

        for row in records:
            question_listbox.insert(tk.END, f"ID {row[0]}: {row[1][:100]}")

    def load_selected_question(event):
        nonlocal selected_id
        selection = question_listbox.get(tk.ACTIVE)
        if not selection:
            return
        selected_id = selection.split(":")[0].replace("ID", "").strip()

        conn = sqlite3.connect("database/quiz_bowl.db")
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT question, option_a, option_b, option_c, option_d, correct_option
            FROM {current_table} WHERE id = ?
        """, (selected_id,))
        result = cursor.fetchone()
        conn.close()

        if result:
            for i, key in enumerate(form_labels):
                form_entries[key].delete(0, tk.END)
                form_entries[key].insert(0, result[i])

    def update_question():
        if not selected_id:
            messagebox.showwarning("Warning", "Select a question to edit first.")
            return

        updated_values = [form_entries[label].get().strip() for label in form_labels]
        if not all(updated_values):
            messagebox.showerror("Error", "All fields must be filled out.")
            return

        conn = sqlite3.connect("database/quiz_bowl.db")
        cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE {current_table}
            SET question = ?, option_a = ?, option_b = ?, option_c = ?, option_d = ?, correct_option = ?
            WHERE id = ?
        """, (*updated_values, selected_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Question updated successfully!")
        load_questions()

    def delete_selected_question():
        if not selected_id:
            messagebox.showwarning("Warning", "Select a question to delete first.")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this question?")
        if not confirm:
            return

        conn = sqlite3.connect("database/quiz_bowl.db")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {current_table} WHERE id = ?", (selected_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Deleted", "Question deleted successfully.")
        for entry in form_entries.values():
            entry.delete(0, tk.END)
        load_questions()

    # Event bindings and buttons
    question_listbox.bind("<<ListboxSelect>>", load_selected_question)

    tk.Button(window, text="Load Questions", command=load_questions).pack()
    tk.Button(window, text="Update Question", command=update_question).pack(pady=5)
    tk.Button(window, text="Delete Selected Question", command=delete_selected_question).pack(pady=5)
    tk.Button(window, text="Back", command=window.destroy).pack(pady=10)

    window.mainloop()

