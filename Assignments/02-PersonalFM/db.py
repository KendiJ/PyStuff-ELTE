import sqlite3
from datetime import datetime

DB_NAME = "finance.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Accounts Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            currency TEXT NOT NULL
        )
    ''')

    # 2. Transactions Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER,
            date TEXT,
            amount REAL,
            type TEXT,
            category TEXT,
            note TEXT,
            FOREIGN KEY (account_id) REFERENCES accounts (id)
        )
    ''')

    # 3. Income Table 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS income (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER,
            date TEXT,
            amount REAL,
            source TEXT,
            FOREIGN KEY (account_id) REFERENCES accounts (id)
        )
    ''')
    
    conn.commit()
    conn.close()

# CRUD Operations 

def add_account(name, currency):
    conn = get_db_connection()
    conn.execute('INSERT INTO accounts (name, currency) VALUES (?, ?)', (name, currency))
    conn.commit()
    conn.close()

def get_accounts():
    conn = get_db_connection()
    rows = conn.execute('SELECT * FROM accounts').fetchall()
    conn.close()
    return [dict(row) for row in rows]

def add_transaction(account_id, date, amount, t_type, category, note):
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO transactions (account_id, date, amount, type, category, note)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (account_id, date, amount, t_type, category, note))
    conn.commit()
    conn.close()

def get_transactions(start_date=None, end_date=None):
    conn = get_db_connection()
    query = "SELECT * FROM transactions"
    params = []
    
    if start_date and end_date:
        query += " WHERE date BETWEEN ? AND ?"
        params = [start_date, end_date]
        
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [dict(row) for row in rows]

def add_income(account_id, date, amount, source):
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO income (account_id, date, amount, source)
        VALUES (?, ?, ?, ?)
    ''', (account_id, date, amount, source))
    conn.commit()
    conn.close()

def get_income():
    conn = get_db_connection()
    rows = conn.execute('SELECT * FROM income').fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_monthly_income():
    conn = get_db_connection()
    query = '''
        SELECT strftime('%Y-%m', date) as month, SUM(amount) as total
        FROM income
        GROUP BY month
        ORDER BY month
    '''
    rows = conn.execute(query).fetchall()
    conn.close()
    return [dict(row) for row in rows]