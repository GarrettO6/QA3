import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from admin.add_question import COURSE_CATEGORIES

def open_view_questions():
    window = tk.Tk()
    window.title("View Questions")
    window.geometry("800x400")

    tk.Label(window, text="Select Course Category").pack()

    category_dropdown = ttk.Combobox(window, state='readonly')
    category_dropdown['values'] = list(COURSE_CATEGORIES.keys())
    category_dropdown.pack(pady=5)

    # ⭐ Force dropdown to show first item on launch
    def set_default_dropdown():
        category_dropdown.current(0)
        print(f"[DEBUG] Forcing selection to: {category_dropdown.get()}")

    window.after(100, set_default_dropdown)  # ⭐ Trigger after window loads

    text_area = tk.Text(window, wrap="word", width=100, height=20)
    text_area.pack(pady=10)

    def load_questions():
        selected_category = category_dropdown.get()
        print(f"[DEBUG] Dropdown value: '{selected_category}'")

        if not selected_category:
            messagebox.showwarning("No Category", "No category detected from dropdown.")
            return

        table = COURSE_CATEGORIES.get(selected_category)
        print(f"[DEBUG] Resolved table: {table}")
        if not table:
            messagebox.showerror("Error", "Course category did not map to a table.")
            return

        try:
            conn = sqlite3.connect("quiz_bowl.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT id, question FROM {table}")
            records = cursor.fetchall()
            conn.close()
        except Exception as e:
            print(f"[DEBUG] Database error: {e}")
            messagebox.showerror("Database Error", str(e))
            return

        print(f"[DEBUG] {len(records)} question(s) loaded.")
        text_area.delete("1.0", tk.END)

        if not records:
            text_area.insert(tk.END, "No questions found for this category.")
            messagebox.showinfo("No Questions", "This category has no questions.")
            return

        for row in records:
            text_area.insert(tk.END, f"ID {row[0]}: {row[1]}\n\n")

    tk.Button(window, text="Load Questions", command=lambda: load_questions()).pack()
    tk.Button(window, text="Back", command=window.destroy).pack(pady=10)

    window.mainloop()

