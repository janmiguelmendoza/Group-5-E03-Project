import tkinter as tk
from tkinter import simpledialog, messagebox
from user import User

class Admin(User):
    def __init__(self, user_id, name, email, password, db, main_window):
        super().__init__(user_id, name, email, password)
        self.db = db
        self.main_window = main_window

    def login(self):
        email = simpledialog.askstring("Admin Login", "Enter your email:", parent=self.main_window)
        password = simpledialog.askstring("Admin Login", "Enter your password:", show='*', parent=self.main_window)
        user = self.db.fetchone('SELECT * FROM user WHERE email = ? AND password = ? AND role = ?', (email, password, 'admin'))
        if user:
            messagebox.showinfo("Login Successful", "Welcome, Admin!", parent=self.main_window)
            self.open_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!", parent=self.main_window)

    def open_dashboard(self):
        admin_window = tk.Toplevel(self.main_window)
        admin_window.title("Admin Dashboard")
        admin_window.geometry("600x400")
        label = tk.Label(admin_window, text="Admin Dashboard")
        label.pack(pady=10)
        manage_users_button = tk.Button(admin_window, text="Manage Users", command=self.manage_users)
        manage_users_button.pack(pady=5)
        manage_jobs_button = tk.Button(admin_window, text="Manage Jobs", command=self.manage_jobs)
        manage_jobs_button.pack(pady=5)

    def manage_users(self):
        # Logic for managing users
        messagebox.showinfo("Manage Users", "Functionality to manage users goes here.", parent=self.main_window)

    def manage_jobs(self):
        # Logic for managing jobs
        messagebox.showinfo("Manage Jobs", "Functionality to manage jobs goes here.", parent=self.main_window)
