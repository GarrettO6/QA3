import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from admin.add_question import COURSE_CATEGORIES

def open_edit_question():
    window = tk.Tk()
    window.title("Edit/Delete Questions")
    window.geometry("850x650")

    tk.Label(window, text="Select Course Category").pack()

    category_dropdown = ttk.Combobox(window, state='readonly')
    category_dropdown['values'] = list(COURSE_CATEGORIES.keys())
    category_dropdown.pack(pady=5)

    window.after(100, lambda: category_dropdown.current(0))  # Force default selection

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
        selected_category = category_dropdown.get()
        print(f"[DEBUG] Selected category: {selected_category}")

        current_table = COURSE_CATEGORIES.get(selected_category)
        if not current_table:
            messagebox.showerror("Error", "Invalid category selected.")
            return

        try:
            conn = sqlite3.connect("quiz_bowl.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT id, question FROM {current_table}")
            records = cursor.fetchall()
            conn.close()
        except Exception as e:
            print(f"[DEBUG] Database error: {e}")
            messagebox.showerror("Database Error", str(e))
            return

        question_listbox.delete(0, tk.END)
        for row in records:
            question_listbox.insert(tk.END, f"ID {row[0]}: {row[1][:100]}")
        print(f"[DEBUG] Loaded {len(records)} questions.")

    def load_selected_question(event):
        nonlocal selected_id
        selection = question_listbox.get(tk.ACTIVE)
        if not selection:
            return
        selected_id = selection.split(":")[0].replace("ID", "").strip()

        try:
            conn = sqlite3.connect("quiz_bowl.db")
            cursor = conn.cursor()
            cursor.execute(f"""
                SELECT question, option_a, option_b, option_c, option_d, correct_option
                FROM {current_table} WHERE id = ?
            """, (selected_id,))
            result = cursor.fetchone()
            conn.close()
        except Exception as e:
            print(f"[DEBUG] Failed to load selected question: {e}")
            return

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

        try:
            conn = sqlite3.connect("quiz_bowl.db")
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
        except Exception as e:
            print(f"[DEBUG] Failed to update question: {e}")
            messagebox.showerror("Database Error", str(e))

    def delete_selected_question():
        if not selected_id:
            messagebox.showwarning("Warning", "Select a question to delete first.")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this question?")
        if not confirm:
            return

        try:
            conn = sqlite3.connect("quiz_bowl.db")
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {current_table} WHERE id = ?", (selected_id,))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"[DEBUG] Failed to delete question: {e}")
            messagebox.showerror("Database Error", str(e))
            return

        messagebox.showinfo("Deleted", "Question deleted successfully.")
        for entry in form_entries.values():
            entry.delete(0, tk.END)
        load_questions()

    # Bindings and Buttons
    question_listbox.bind("<<ListboxSelect>>", load_selected_question)

    tk.Button(window, text="Load Questions", command=lambda: load_questions()).pack()
    tk.Button(window, text="Update Question", command=lambda: update_question()).pack(pady=5)
    tk.Button(window, text="Delete Selected Question", command=lambda: delete_selected_question()).pack(pady=5)
    tk.Button(window, text="Back", command=window.destroy).pack(pady=10)

    window.mainloop()

