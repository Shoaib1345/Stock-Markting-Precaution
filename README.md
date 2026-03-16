Crypto Price Predictor
Overview

Crypto Price Predictor is a Python desktop application that allows users to log in, register, and view cryptocurrency price predictions. The system stores user accounts and prediction history using a SQLite database.

The application provides a simple interface where users can work with different cryptocurrency symbols and save prediction data.

Features

User Login System

User Registration System

SQLite Database for storing users and predictions

Support for multiple cryptocurrency symbols

Store predicted prices and prediction time

Clean and simple GUI interface

Technologies Used

Python

Tkinter (GUI)

SQLite3 (Database)

JSON

CSV

Datetime

Project Structure
project-folder
│
├── main.py
├── users.db
├── crypto_predictions.db
├── README.md
Database Tables
Users Table
Column	Description
id	User ID
username	User name
password	User password
Predictions Table
Column	Description
id	Prediction ID
symbol	Cryptocurrency symbol
predicted_at	Prediction date and time
hours	Number of hours predicted
predicted_prices	Stored predicted prices
Supported Cryptocurrencies

The application supports the following symbols:

BTCUSDT

ETHUSDT

BNBUSDT

XRPUSDT

ADAUSDT

DOGEUSDT

SOLUSDT

MATICUSDT

DOTUSDT

TRXUSDT

LTCUSDT

SHIBUSDT

AVAXUSDT

BCHUSDT

ETCUSDT

LINKUSDT

NEARUSDT

Installation
1 Install Python

Make sure Python is installed.

2 Clone the repository
git clone https://github.com/yourusername/crypto-price-predictor.git
3 Open the project folder
cd crypto-price-predictor
4 Run the program
python main.py
How It Works

User opens the application.

User registers or logs in.

After login, the main Crypto Predictor window opens.

The system stores prediction data in the database.

Users can access stored prediction records.

Security Note

Currently passwords are stored as plain text in the database. For better security, password hashing should be implemented.

Future Improvements

Add machine learning model for better prediction

Add real-time crypto price API

Add data visualization charts

Add password encryption

Export prediction results to CSV

Author

Shoaib Ahmed

Student of Artificial Intelligence
Interested in AI, Machine Learning, and Software Development.
