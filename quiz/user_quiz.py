import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import random
from admin.add_question import COURSE_CATEGORIES  # Reuse category list

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl")
        self.root.geometry("600x400")

        self.score = 0
        self.current_question_index = 0
        self.questions = []

        self.build_category_selection()

    def build_category_selection(self):
        self.clear_window()

        tk.Label(self.root, text="Select Quiz Category", font=("Arial", 16)).pack(pady=20)
        self.category_var = tk.StringVar()
        category_menu = ttk.Combobox(self.root, textvariable=self.category_var, values=list(COURSE_CATEGORIES.keys()), state='readonly')
        category_menu.pack(pady=10)

        tk.Button(self.root, text="Start Quiz", command=self.start_quiz).pack(pady=20)

    def start_quiz(self):
        selected_category = self.category_var.get()
        if not selected_category:
            messagebox.showwarning("Warning", "Please select a category.")
            return

        table_name = COURSE_CATEGORIES[selected_category]

        conn = sqlite3.connect("quiz_bowl.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, question, option_a, option_b, option_c, option_d, correct_option FROM {table_name}")
        self.questions = cursor.fetchall()
        conn.close()

        if not self.questions:
            messagebox.showinfo("No Questions", "No questions available for this category.")
            return

        random.shuffle(self.questions)
        self.score = 0
        self.current_question_index = 0
        self.show_question()

    def show_question(self):
        self.clear_window()

        if self.current_question_index >= len(self.questions):
            self.show_final_score()
            return

        q = self.questions[self.current_question_index]
        self.current_question_id = q[0]
        question_text = q[1]
        options = q[2:6]
        self.correct_answer = q[6].upper()

        tk.Label(self.root, text=f"Question {self.current_question_index + 1}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text=question_text, wraplength=500, font=("Arial", 12)).pack(pady=10)

        self.answer_var = tk.StringVar()

        for i, opt in enumerate(["A", "B", "C", "D"]):
            rb = tk.Radiobutton(self.root, text=f"{opt}: {options[i]}", variable=self.answer_var, value=opt, font=("Arial", 11))
            rb.pack(anchor='w', padx=50)

        tk.Button(self.root, text="Submit Answer", command=self.check_answer).pack(pady=20)

    def check_answer(self):
        selected = self.answer_var.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        if selected.upper() == self.correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "That's the right answer!")
        else:
            messagebox.showinfo("Incorrect", f"The correct answer was {self.correct_answer}.")

        self.current_question_index += 1
        self.show_question()

    def show_final_score(self):
        self.clear_window()
        tk.Label(self.root, text="Quiz Completed!", font=("Arial", 18)).pack(pady=30)
        tk.Label(self.root, text=f"Your Score: {self.score} out of {len(self.questions)}", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Take Another Quiz", command=self.build_category_selection).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def open_quiz_ui():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
