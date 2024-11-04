import tkinter as tk
from tkinter import filedialog, messagebox
from data_analysis import DataAnalysis
from auth import Auth

class DataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Analysis and Prediction")

        self.auth = Auth(self.root, self.load_main_ui)
        self.auth.login_ui()

    def load_main_ui(self):
        self.data_analysis = DataAnalysis(self.root)
        self.data_analysis.create_ui()

if __name__ == "__main__":
    root = tk.Tk()
    app = DataApp(root)
    root.mainloop()
