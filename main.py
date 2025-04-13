

import tkinter as tk
from gui.admin_login import launch_admin_login
from gui.quiz_login import launch_quiz_login

def main():
    root = tk.Tk()
    root.title("Quiz Bowl - Login")
    root.geometry("300x200")

    tk.Label(root, text="Welcome to Quiz Bowl!", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="Admin Login", width=20, command=lambda: launch_admin_login(root)).pack(pady=5)
    tk.Button(root, text="Take a Quiz", width=20, command=lambda: launch_quiz_login(root)).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()


