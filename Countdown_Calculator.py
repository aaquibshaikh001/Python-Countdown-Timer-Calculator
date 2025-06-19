import tkinter as tk
from tkinter import messagebox, ttk
import threading
import time
import sqlite3
import pandas as pd


# ===== DATABASE SETUP =====
def init_db():
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS calculations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    operation TEXT,
                    result REAL
                )''')
    conn.commit()
    conn.close()


def save_to_db(operation, result):
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    c.execute("INSERT INTO calculations (operation, result) VALUES (?, ?)", (operation, result))
    conn.commit()
    conn.close()


def export_to_csv():
    try:
        conn = sqlite3.connect('history.db')
        df = pd.read_sql_query("SELECT * FROM calculations", conn)
        df.to_csv("calculation_history.csv", index=False)
        conn.close()
        messagebox.showinfo("Export Successful", "Exported to 'calculation_history.csv'")
    except Exception as e:
        messagebox.showerror("Export Failed", str(e))


# ===== TIMER LOGIC =====
def start_countdown(entry, label):
    try:
        time_input = entry.get().strip().lower()
        if time_input.endswith("s"):
            total_seconds = int(time_input[:-1])
        elif time_input.endswith("m"):
            total_seconds = int(time_input[:-1]) * 60
        else:
            raise ValueError("Invalid format! Use 'm' for minutes or 's' for seconds.")

        def countdown():
            remaining = total_seconds
            while remaining > 0:
                mins, secs = divmod(remaining, 60)
                label.config(text=f"{mins:02d}:{secs:02d}")
                time.sleep(1)
                remaining -= 1
            label.config(text="Time's up!")
            messagebox.showinfo("Timer", "⏰ Time's up!")

        threading.Thread(target=countdown, daemon=True).start()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ===== CALCULATOR LOGIC =====
def calculate(entry, result_label):
    expression = entry.get()
    try:
        result = round(eval(expression), 2)  # still using eval, consider using ast.literal_eval or math parser
        result_label.config(text=f"Result: {result}")
        save_to_db(expression, result)
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")
    except Exception:
        messagebox.showerror("Input Error", "Invalid mathematical expression!")


# ===== GUI STRUCTURE =====
def setup_timer_tab(frame):
    tk.Label(frame, text="Enter Time (e.g., 10s or 1m):", font=("Helvetica", 12)).pack(pady=10)
    timer_entry = tk.Entry(frame, font=("Helvetica", 12), width=20, justify='center')
    timer_entry.pack(pady=5)
    timer_label = tk.Label(frame, text="00:00", font=("Helvetica", 28), fg="blue")
    timer_label.pack(pady=15)
    tk.Button(frame, text="Start Countdown", font=("Helvetica", 12), command=lambda: start_countdown(timer_entry, timer_label)).pack(pady=10)

    # Bind Enter key
    timer_entry.bind("<Return>", lambda event: start_countdown(timer_entry, timer_label))


def setup_calculator_tab(frame):
    tk.Label(frame, text="Enter Expression (e.g., 2 + 3 * 4):", font=("Helvetica", 12)).pack(pady=10)
    expr_entry = tk.Entry(frame, font=("Helvetica", 12), width=25, justify='center')
    expr_entry.pack(pady=5)
    result_label = tk.Label(frame, text="Result: ", font=("Helvetica", 14), fg="green")
    result_label.pack(pady=10)

    btn_frame = tk.Frame(frame)
    btn_frame.pack(pady=5)

    tk.Button(btn_frame, text="Calculate", font=("Helvetica", 12), width=12, command=lambda: calculate(expr_entry, result_label)).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Export to CSV", font=("Helvetica", 12), width=12, command=export_to_csv).grid(row=0, column=1, padx=5)

    # Bind Enter key
    expr_entry.bind("<Return>", lambda event: calculate(expr_entry, result_label))


# ===== MAIN APP WINDOW =====
def main():
    init_db()

    root = tk.Tk()
    root.title("🧮 Countdown Timer & Calculator")
    root.geometry("400x500")
    root.resizable(False, False)

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both")

    timer_frame = tk.Frame(notebook, bg="#f0f0f0")
    calc_frame = tk.Frame(notebook, bg="#f0f0f0")

    setup_timer_tab(timer_frame)
    setup_calculator_tab(calc_frame)

    notebook.add(timer_frame, text="⏱ Countdown Timer")
    notebook.add(calc_frame, text="🧮 Calculator")

    root.mainloop()


if __name__ == "__main__":
    main()
