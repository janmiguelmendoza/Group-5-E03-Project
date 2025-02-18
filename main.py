import os
import tkinter as tk
from tkinter import messagebox, simpledialog
from helper import Database
from admin import Admin
from employer import Employer
from applicant import Applicant

# Initialize the database if not already done
import database

# Main window setup using Tkinter
window = tk.Tk()
window.title("Job Application Portal")
window.geometry("600x400")

# Define fields and buttons
label1 = tk.Label(window, text="Welcome to the Job Application Portal")
label1.pack(pady=10)

# Initialize the database connection
db = Database('database_folder/job_portal.db')

# Manually insert an admin record (for testing purposes)
admin = Admin(1, 'Admin Name', 'admin@example.com', 'admin_password', db, window)
admin.save(db)

# Initialize user functions
admin_functions = Admin(1, "Admin Name", "admin@example.com", "admin_password", db, window)
employer_functions = Employer(2, "Employer Name", "employer@example.com", "employer_password", db, window)
applicant_functions = Applicant(3, "Applicant Name", "applicant@example.com", "applicant_password", db, window)

# Admin Login
admin_button = tk.Button(window, text="Admin Login", command=admin_functions.login)
admin_button.pack(pady=5)

# Employer Login
employer_button = tk.Button(window, text="Employer Login", command=employer_functions.login)
employer_button.pack(pady=5)

# Applicant Login
applicant_button = tk.Button(window, text="Applicant Login", command=applicant_functions.login)
applicant_button.pack(pady=5)

window.mainloop()
