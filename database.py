import sqlite3

DB_NAME = "finance.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            note TEXT,
            date TEXT DEFAULT (DATE('now'))
        )
    """)
    conn.commit()
    conn.close()

def add_transaction(type_, category, amount, note=""):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (type, category, amount, note) VALUES (?, ?, ?, ?)",
        (type_, category, amount, note)
    )
    conn.commit()
    conn.close()
    print("Added: " + type_ + " of " + str(amount))

def view_all():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, type, category, amount, note FROM transactions ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        print("No transactions yet.")
        return
    print("\nID | Date | Type | Category | Amount | Note")
    print("-" * 50)
    for row in rows:
        print(str(row[0]) + " | " + row[1] + " | " + row[2] + " | " + row[3] + " | " + str(row[4]) + " | " + str(row[5]))

def summary():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    total_income = cursor.fetchone()[0] or 0
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    total_expense = cursor.fetchone()[0] or 0
    cursor.execute("SELECT category, type, SUM(amount) FROM transactions GROUP BY category, type ORDER BY type, category")
    by_category = cursor.fetchall()
    conn.close()
    print("\nSUMMARY")
    print("Total Income  : " + str(total_income))
    print("Total Expense : " + str(total_expense))
    print("Balance       : " + str(total_income - total_expense))
    print("\nBy Category:")
    for cat, typ, amt in by_category:
        print("  [" + typ.upper() + "] " + cat + ": " + str(amt))
