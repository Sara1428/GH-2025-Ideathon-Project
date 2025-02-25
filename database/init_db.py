import sqlite3
import os

def init_db():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect("database/pharmacy.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS medicines (
                        id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        stock INTEGER)''')
    cursor.executemany("INSERT INTO medicines (name, stock) VALUES (?, ?)", 
                       [("Paracetamol", 50), ("Ibuprofen", 30), ("Amoxicillin", 20)])
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
