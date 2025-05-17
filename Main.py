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

        self.current_user = None
        self.symbol_list = [
            "BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT", "DOGEUSDT",
            "SOLUSDT", "MATICUSDT", "DOTUSDT", "TRXUSDT", "LTCUSDT", "SHIBUSDT",
            "AVAXUSDT", "BCHUSDT", "ETCUSDT", "LINKUSDT", "NEARUSDT"
        ]

        self.setup_database()
        self.create_login_screen()
