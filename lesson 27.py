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

def autorixation():
    user_login = str(input("input log: "))
    test = cursor.execute('SELECT id FROM users WHERE login = ?',
                     (user_login, ))
    if test.fetchone() is not None:
        print('hello')
    else:
        ('i dont know who u are')

def create_product():
    try:
        cursor.execute(''' CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price FLOAT NOT NUll,
        count INTEGER
    )
''')
        print("sucessfuly start")
    except Exception as ex:
        print('donr work')
        print(ex)
def add_product():
    name_products = str(input('input name of product: '))
    price_products = str(input('input name of product: '))
    count_products = str(input("input count of products"))
    cursor.execute ("INSERT INTO product (name, price, count) VALUES (?, ?, ?)",
                    (name_products, price_products, count_products))
    conn.commit()
def find_product():
    find_name_product = str(input('which product u search'))
    find_product_cart = '%' + find_name_product + '%' 
    cursor.execute(
        "SELECT * FROM product WHERE name LIKE ? ", (find_product_cart, )
    )
    rows = cursor.fetchall()
    if rows:
        for i in rows:       
            print(i[1], i[2])
    else:
        print('i dont find this product')
        
    
        

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
            autorixation()
            action = str(input("your move: "))
            if action == "shop":
                create_product()
                add_my_product = str(input("add your product: ")). lower()
                add_product()
                find_product()
                
        