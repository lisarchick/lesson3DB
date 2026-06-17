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

    except Exception as ex:
        print("dont start ERORR")
        print(ex)

def create_user(name,login,age):
    cursor.execute('INSERT INTO users (name, login, age) VALUES(?, ?, ?)',
                   (name,login,age))
                    
    

    conn.commit()
def add_balance(balance,login):
    cursor.execute('UPDATE users SET balance = ? WHERE login = ?', 
                   (balance, login))
    conn.commit()

if __name__ == "__main__":
    question = str(input("register or log in ?"))
    create_db()
    if question == "register".lower():
        name = str(input("your name: "))
        login = str(input("your login: "))
        age = int(input("your age: "))
        create_user(name,login,age)
        while True:
            balance = float(input("add your balance sir: "))
            add_balance(balance, login)
    elif question == "log in".lower():
        pass