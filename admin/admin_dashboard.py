import tkinter as tk
from add_question import open_add_question
from view_questions import open_view_questions
from edit_question import open_edit_question


def open_admin_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Admin Dashboard")
    dashboard.geometry("300x250")

    tk.Label(dashboard, text="Welcome, Admin!", font=("Arial", 14)).pack(pady=10)

    tk.Button(dashboard, text="➕ Add New Question", width=25, command=open_add_question).pack(pady=5)
    tk.Button(dashboard, text="📋 View Questions", width=25, command=open_view_questions).pack(pady=5)
    tk.Button(dashboard, text="🛠️ Edit/Delete Questions", width=25, command=open_edit_question).pack(pady=5)


    tk.Button(dashboard, text="🚪 Logout", width=25, command=dashboard.destroy).pack(pady=20)

    dashboard.mainloop()
