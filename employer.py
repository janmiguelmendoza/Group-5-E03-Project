import tkinter as tk
from tkinter import simpledialog, messagebox
from user import User

class Employer(User):
    def __init__(self, user_id, name, email, password, db, main_window):
        super().__init__(user_id, name, email, password)
        self.db = db
        self.main_window = main_window

    def login(self):
        email = simpledialog.askstring("Employer Login", "Enter your email:", parent=self.main_window)
        password = simpledialog.askstring("Employer Login", "Enter your password:", show='*', parent=self.main_window)
        user = self.db.fetchone('SELECT * FROM user WHERE email = ? AND password = ? AND role = ?', (email, password, 'employer'))
        if user:
            messagebox.showinfo("Login Successful", "Welcome, Employer!", parent=self.main_window)
            self.open_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!", parent=self.main_window)

    def open_dashboard(self):
        employer_window = tk.Toplevel(self.main_window)
        employer_window.title("Employer Dashboard")
        employer_window.geometry("600x400")
        label = tk.Label(employer_window, text="Employer Dashboard")
        label.pack(pady=10)
        
        post_job_button = tk.Button(employer_window, text="Post Job", command=self.post_job)
        post_job_button.pack(pady=5)
        
        view_applications_button = tk.Button(employer_window, text="View Applications", command=self.view_applications)
        view_applications_button.pack(pady=5)
        
        update_job_listings_button = tk.Button(employer_window, text="Update Job Listings", command=self.update_job_listings)
        update_job_listings_button.pack(pady=5)

    def post_job(self):
        # Logic for posting a new job
        messagebox.showinfo("Post Job", "Functionality to post a new job goes here.", parent=self.main_window)

    def view_applications(self):
        # Logic for viewing applications
        messagebox.showinfo("View Applications", "Functionality to view applications goes here.", parent=self.main_window)

    def update_job_listings(self):
        # Logic for updating job listings
        messagebox.showinfo("Update Job Listings", "Functionality to update job listings goes here.", parent=self.main_window)
