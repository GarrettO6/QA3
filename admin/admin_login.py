import tkinter as tk
from tkinter import messagebox
from admin_dashboard import open_admin_dashboard  # Make sure this file exists next

# Hardcoded admin credentials
ADMIN_PASSWORD = "admin123"

def verify_password():
    entered = password_entry.get()
    if entered == ADMIN_PASSWORD:
        root.destroy()
        open_admin_dashboard()
    else:
        messagebox.showerror("Access Denied", "Incorrect password.")

# GUI Setup
root = tk.Tk()
root.title("Admin Login")
root.geometry("300x150")

tk.Label(root, text="Enter Admin Password:").pack(pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=verify_password).pack(pady=10)

root.mainloop()
