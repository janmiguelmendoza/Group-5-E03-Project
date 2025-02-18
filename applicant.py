import tkinter as tk
from tkinter import simpledialog, messagebox
from user import User

class Applicant(User):
    def __init__(self, user_id, name, email, password, db, main_window):
        super().__init__(user_id, name, email, password)
        self.db = db
        self.main_window = main_window

    def login(self):
        email = simpledialog.askstring("Applicant Login", "Enter your email:", parent=self.main_window)
        password = simpledialog.askstring("Applicant Login", "Enter your password:", show='*', parent=self.main_window)
        user = self.db.fetchone('SELECT * FROM user WHERE email = ? AND password = ? AND role = ?', (email, password, 'applicant'))
        if user:
            messagebox.showinfo("Login Successful", "Welcome, Applicant!", parent=self.main_window)
            self.open_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!", parent=self.main_window)

    def open_dashboard(self):
        applicant_window = tk.Toplevel(self.main_window)
        applicant_window.title("Applicant Dashboard")
        applicant_window.geometry("600x400")
        label = tk.Label(applicant_window, text="Applicant Dashboard")
        label.pack(pady=10)
        
        search_jobs_button = tk.Button(applicant_window, text="Search Jobs", command=self.search_jobs)
        search_jobs_button.pack(pady=5)
        
        apply_for_job_button = tk.Button(applicant_window, text="Apply for Job", command=self.apply_for_job)
        apply_for_job_button.pack(pady=5)
        
        update_profile_button = tk.Button(applicant_window, text="Update Profile", command=self.update_profile)
        update_profile_button.pack(pady=5)

    def search_jobs(self):
        # Logic for searching for jobs
        messagebox.showinfo("Search Jobs", "Functionality to search for jobs goes here.", parent=self.main_window)

    def apply_for_job(self):
        # Logic for applying for a job
        messagebox.showinfo("Apply for Job", "Functionality to apply for a job goes here.", parent=self.main_window)

    def update_profile(self):
        # Logic for updating profile
        messagebox.showinfo("Update Profile", "Functionality to update profile goes here.", parent=self.main_window)
