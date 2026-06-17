import sqlite3
with sqlite3.connect("shop.db") as conn:
    cursor = conn.cursor()
def create_db():
    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            login TEXT NOT NULL,
            age INTEGER,
            balance REAL DEFAULT 0.0  
                    )
    ''')
        print("SUCESFULY start")
        conn.commit()
        conn.close()
    except Exception as ex:
        print("dont start ERORR")
        print(ex)

if __name__ == "__main__":
    create_db()