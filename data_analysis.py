import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog, messagebox
import tkinter as tk
from sklearn.linear_model import LinearRegression
import numpy as np

class DataAnalysis:
    def __init__(self, root):
        self.root = root
        self.df = None

    def create_ui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.import_btn = tk.Button(self.frame, text="Import CSV", command=self.import_csv)
        self.import_btn.grid(row=0, column=0, padx=10)

        self.process_btn = tk.Button(self.frame, text="Process Data", command=self.process_data)
        self.process_btn.grid(row=0, column=1, padx=10)

        self.visualize_btn = tk.Button(self.frame, text="Visualize Data", command=self.visualize_data)
        self.visualize_btn.grid(row=0, column=2, padx=10)

        self.predict_btn = tk.Button(self.frame, text="Predict Sales", command=self.predict_sales)
        self.predict_btn.grid(row=0, column=3, padx=10)

    def import_csv(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                self.df = pd.read_csv(file_path, delimiter=';')  # Specify the delimiter
                self.df.columns = self.df.columns.str.strip()  # Strip any whitespace from the column headers
                print(f"Columns in CSV: {self.df.columns}")  # Debug: Print column headers
                if 'Date' not in self.df.columns or 'Sales' not in self.df.columns:
                    raise ValueError("CSV file must contain 'Date' and 'Sales' columns")
                messagebox.showinfo("Info", "Dataset imported successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to import CSV: {e}")

    def process_data(self):
        if self.df is not None:
            try:
                self.df.dropna(inplace=True)
                self.df['Date'] = pd.to_datetime(self.df['Date'])
                self.df['Sales'] = pd.to_numeric(self.df['Sales'])
                messagebox.showinfo("Info", "Data processed successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to process data: {e}")
        else:
            messagebox.showwarning("Warning", "No data to process.")

    def visualize_data(self):
        if self.df is not None:
            try:
                plt.figure(figsize=(10, 6))
                plt.plot(self.df['Date'], self.df['Sales'])
                plt.title('Sales Trend')
                plt.xlabel('Date')
                plt.ylabel('Sales')
                plt.show()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to visualize data: {e}")
        else:
            messagebox.showwarning("Warning", "No data to visualize.")

    def predict_sales(self):
        if self.df is not None:
            try:
                self.df['Month'] = self.df['Date'].dt.month
                X = self.df[['Month']].values
                y = self.df['Sales'].values

                model = LinearRegression()
                model.fit(X, y)

                future_months = np.array([[i] for i in range(1, 13)])
                predictions = model.predict(future_months)

                plt.figure(figsize=(10, 6))
                plt.plot(future_months, predictions, label='Predicted Sales')
                plt.title('Sales Prediction')
                plt.xlabel('Month')
                plt.ylabel('Sales')
                plt.legend()
                plt.show()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to predict sales: {e}")
        else:
            messagebox.showwarning("Warning", "No data to predict.")
