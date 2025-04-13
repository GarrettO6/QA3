import tkinter as tk
from tkinter import simpledialog, messagebox
from admin.admin_dashboard import open_admin_dashboard
from quiz.user_quiz import open_quiz_ui

# Admin password 
ADMIN_PASSWORD = "gClaryROX"

def open_main_window():
    root = tk.Tk()
    root.title("Quiz Bowl Application")
    root.geometry("400x300")

    tk.Label(root, text="Welcome to the Quiz Bowl App", font=("Arial", 16)).pack(pady=30)

    tk.Button(root, text="Administrator Login", width=25, height=2, command=lambda: handle_admin_login(root)).pack(pady=10)
    tk.Button(root, text="Take a Quiz", width=25, height=2, command=lambda: open_quiz_ui_from_main(root)).pack(pady=10)

    root.mainloop()

def handle_admin_login(root_window):
    password = simpledialog.askstring("Admin Login", "Enter admin password:", show="*")
    if password == ADMIN_PASSWORD:
        root_window.destroy()  # Close main window
        open_admin_dashboard()
    else:
        messagebox.showerror("Access Denied", "Incorrect password!")

def open_quiz_ui_from_main(root_window):
    root_window.destroy()  # Close main window
    open_quiz_ui()

if __name__ == "__main__":
    open_main_window()
