# ⏱️ Countdown Timer & 🧮 Calculator App in Python

This is a dual-purpose Python application that combines a **countdown timer** and a **basic calculator**. It offers both console-based interaction and the optional flexibility of a GUI (using Tkinter) and persistent history storage (using SQLite).

---

## 🚀 Features

### ⏳ Countdown Timer:
- Set countdown in **seconds** or **minutes**
- Console-based alert or popup (Tkinter-based optional)
- Timer runs asynchronously using Python’s `threading` module

### 🧮 Basic Calculator:
- Supports **Addition**, **Subtraction**, **Multiplication**, and **Division**
- Handles **integer** and **decimal** inputs
- Prevents invalid operations (e.g., division by zero)
- Error handling for non-numeric input

### 📜 Optional Enhancements:
- GUI with Tkinter (Input fields, buttons, results)
- Operation **history storage** using SQLite
- Generate logs or reports using `logging` and `pandas`

---

## 💻 Technologies Used

- **Python 3**
- `time`, `threading`, `math`, `sqlite3`, `logging` (standard libraries)
- `Tkinter` *(optional GUI)*
- `pandas` *(optional reporting)*

---

## 🧩 File Structure

📁 Python-Countdown-Timer-Calculator/
├── main.py # Core logic for calculator and timer
├── gui_app.py # Optional Tkinter GUI implementation
├── database.py # SQLite integration for history (optional)
├── utils.py # Utility functions
├── logs/ # Folder to store log files
│ └── app.log
├── reports/ # Folder to store pandas reports (optional)
│ └── report.csv
├── README.md # Project documentation
└── requirements.txt # Python dependencies

yaml
Copy
Edit

---

## 🛠️ How to Run

### 🔹 Console Version:
```bash
python main.py
🔸 GUI Version (if implemented):
bash
Copy
Edit
python gui_app.py
🧪 Example Usage (Console)
bash
Copy
Edit
Select an option:
1. Countdown Timer
2. Calculator

> 1
Enter time in seconds: 10
Timer started...
⏰ Time's up!

> 2
Enter first number: 8
Enter operation (+, -, *, /): *
Enter second number: 6
Result: 48.0
🧠 Optional: SQLite and Reporting
Store calculator history (inputs, operations, results, timestamps)

Export operation logs to CSV using pandas

Example SQLite Table:

sql
Copy
Edit
CREATE TABLE history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    operation TEXT,
    result REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
📈 Future Improvements
Add sound alerts for timer

Add scientific calculator functions (sqrt, log, etc.)

Add countdown timer presets (Pomodoro, study breaks)

User profiles and session tracking

📄 License
This project is licensed under the MIT License.

✍️ Author
Aaquib Shaikh
GitHub: aaqibshaikh001
