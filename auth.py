import tkinter as tk
from tkinter import messagebox
from database import Database

class Auth:
    def __init__(self, root, on_success):
        self.root = root
        self.on_success = on_success
        self.db = Database()

    def login_ui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        tk.Label(self.frame, text="Username").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Password").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        login_btn = tk.Button(self.frame, text="Login", command=self.login)
        login_btn.grid(row=2, column=0, columnspan=2, pady=10)

        register_btn = tk.Button(self.frame, text="Register", command=self.register_ui)
        register_btn.grid(row=3, column=0, columnspan=2, pady=10)

    def register_ui(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        tk.Label(self.frame, text="Username").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Password").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        register_btn = tk.Button(self.frame, text="Register", command=self.register)
        register_btn.grid(row=2, column=0, columnspan=2, pady=10)

        back_btn = tk.Button(self.frame, text="Back to Login", command=self.back_to_login)
        back_btn.grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.db.validate_user(username, password):
            self.frame.destroy()
            self.on_success()
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.db.add_user(username, password):
            messagebox.showinfo("Success", "Registration successful! Please log in.")
            self.back_to_login()
        else:
            messagebox.showerror("Error", "Registration failed. Try a different username.")

    def back_to_login(self):
        self.frame.destroy()
        self.login_ui()
