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
            balance REAL DEFAULT 0.0 ,
            password TEXT NOT NUll
                    )
    ''')
        print("SUCESFULY start")

    except Exception as ex:
        print("dont start ERORR")
        print(ex)

def create_user(name,login,age,password):
    cursor.execute('INSERT INTO users (name, login, age, password) VALUES(?, ?, ?, ?)',
                   (name,login,age, password))
                    
    

    conn.commit()
def add_balance(balance,login):
    cursor.execute('UPDATE users SET balance = ? WHERE login = ?', 
                   (balance, login))
    conn.commit()

def autorixation(vhod):
    user_login = str(input("input log: "))
    user_password = str(input('input password'))
    test = cursor.execute('SELECT id FROM users WHERE login = ? AND password = ?',
                     (user_login,user_password,  ))
    if test.fetchone() is not None :
        print('hello')
        vhod = True
        return vhod
    else:
        ('i dont know who u are')
        return vhod

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
    price_products = float(input('input name of product: '))
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
            print(f" Name: {i[1]},\nprice: {i[2]}rub")
            buy_product(find_name_product)
    else:
        print('i dont find this product')
        
def buy_product(find_name_product):
    buy_product_quantity = int(input("input count of products: "))
    cursor.execute("SELECT name, price, count FROM product WHERE name = ?",
                   (find_name_product, ))
    product = cursor.fetchone()
    if not product:
        print('product dont found')
    else:
        name,price,stock = product
        if buy_product_quantity > stock:
            print('nedostatocho products')
        else:
            new_stock = stock - buy_product_quantity
            cursor.execute("UPDATE product SET count = ? WHERE name = ?", (new_stock,find_name_product))
            conn.commit()
            total_price = price * buy_product_quantity
            print(f" sucessfuly buy{name}\nCount: {buy_product_quantity},\n{total_price:.2f}")
        

if __name__ == "__main__":
    question = str(input("register or log in ?"))
    create_db()
    if question == "register".lower():
        name = str(input("your name: "))
        login = str(input("your login: "))
        age = int(input("your age: "))
        password = str(input("your password: "))
        create_user(name,login,age,password)
        while True:
            balance = float(input("add your balance sir: "))
            add_balance(balance, login)
    elif question == "log in".lower():
            vhod = False
            autorixation(vhod)
            if vhod == False:
                print("goodbuy")
            else:
                action = str(input("your move: "))
                if action == "shop":
                    create_product()
                    add_my_product = str(input("add your product: ")). lower()
                    if add_product == "yes":
                        add_product()
                    else:
                        find_product()
                    


                
        