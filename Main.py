import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from binance.client import Client
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sqlite3
import json
import datetime
import csv

client = Client()

# ---------- Login Window Class ----------
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Crypto Predictor")
        self.root.geometry("400x300")
        self.root.configure(bg="#001f3f")

        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        """)
        self.conn.commit()

        tk.Label(root, text="Username:", font=("Segoe UI", 12), bg="#001f3f", fg="white").pack(pady=10)
        self.username_entry = tk.Entry(root, font=("Segoe UI", 12), bg="#f0f8ff", fg="black")
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Password:", font=("Segoe UI", 12), bg="#001f3f", fg="white").pack(pady=10)
        self.password_entry = tk.Entry(root, font=("Segoe UI", 12), show="*", bg="#f0f8ff", fg="black")
        self.password_entry.pack(pady=5)

        tk.Button(root, text="Login", font=("Segoe UI", 12), bg="#0074D9", fg="white",
                  activebackground="#005fa3", command=self.login).pack(pady=10)
        tk.Button(root, text="Register", font=("Segoe UI", 10), bg="#7FDBFF", fg="black",
                  activebackground="#39CCCC", command=self.register).pack()

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = self.cursor.fetchone()
        if user:
            messagebox.showinfo("Login Success", f"Welcome, {username}!")
            self.root.destroy()
            main_window = tk.Tk()
            app = CryptoPricePredictor(main_window)
            main_window.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def register(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showwarning("Input Error", "Username and password are required.")
            return

        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            messagebox.showinfo("Success", "Registration successful! You can now log in.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")


# ---------- Crypto Predictor Class ----------
class CryptoPricePredictor:
    def __init__(self, root):
        self.root = root
        self.root.title("💰 Crypto Price Predictor")
        self.root.geometry("1050x750")
        self.root.configure(bg="#001f3f")

        self.symbol_list = [
            "BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT", "DOGEUSDT",
            "SOLUSDT", "MATICUSDT", "DOTUSDT", "TRXUSDT", "LTCUSDT", "SHIBUSDT",
            "AVAXUSDT", "BCHUSDT", "ETCUSDT", "LINKUSDT", "NEARUSDT"
        ]

        self.setup_database()
        self.create_tabs()

    def setup_database(self):
        self.conn = sqlite3.connect("crypto_predictions.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT,
                predicted_at TEXT,
                hours INTEGER,
                predicted_prices TEXT
            )
        """)
        self.conn.commit()
