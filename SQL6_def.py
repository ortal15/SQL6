import sqlite3


def create_table():
    import os
    import sqlite3

    if os.path.exists("test_sql.db"):
        os.remove("test_sql.db")
    else:
        print("The file does not exist")
    conn = sqlite3.connect('test_sql.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE products (\
        products_id INTEGER PRIMARY KEY AUTOINCREMENT ,\
        name TEXT NOT NULL ,\
        price REAL DEFAULT 0 CHECK(price >= 0) ,\
        category_id INTEGER NOT NULL ,\
        FOREIGN KEY (category_id) REFERENCES category (category_id)\
    );")
    cursor.execute("CREATE TABLE category (\
        category_id INTEGER PRIMARY KEY AUTOINCREMENT , \
        name TEXT NOT NULL \
    );")
    cursor.execute("CREATE TABLE nutritions (\
        nutrition_id INTEGER PRIMARY KEY AUTOINCREMENT  ,\
        name TEXT NOT NULL ,\
        products_id INTEGER NOT NULL ,\
        calories INTEGER DEFAULT 0 CHECK (calories >= 0) ,\
        fats INTEGER DEFAULT 0 CHECK (fats >= 0) ,\
        sugar INTEGER DEFAULT 0 CHECK (sugar >= 0) ,\
        FOREIGN KEY ( products_id ) REFERENCES products ( products_id )\
    );")
    cursor.execute("CREATE TABLE orders (\
        order_id INTEGER PRIMARY KEY AUTOINCREMENT ,\
        time_date timestamp DEFAULT CURRENT_TIMESTAMP,\
        address TEXT NOT null ,\
        customer_name TEXT ,\
        customer_ph INTEGER NOT NULL ,\
        total_price REAL DEFAULT 0 CHECK( total_price >= 0) \
    );")
    cursor.execute("CREATE TABLE products_orders (\
        order_id  INTEGER NOT NULL ,\
        products_id   INTEGER NOT NULL ,\
        amount INTEGER DEFAULT 0 ,\
        PRIMARY KEY(order_id , products_id),\
        FOREIGN KEY (order_id) REFERENCES orders (order_id),\
        FOREIGN KEY (products_id) REFERENCES products (products_id)\
    );")
    cursor.execute("INSERT INTO category (name) VALUES\
    ('Beverages'),\
    ('Snacks'),\
    ('Dairy'),\
    ('Fruits'),\
    ('Vegetables');")
    cursor.execute("INSERT INTO products (name, price, category_id) VALUES \
    ('Orange Juice', 5.99, 1),\
    ('Chocolate Bar', 2.50, 2),\
    ('Milk', 3.20, 3),\
    ('Apple', 1.50, 4),\
    ('Carrot', 0.99, 5),\
    ('Coca Cola', 1.50, 1),  \
    ('Pepsi', 1.40, 1),    \
    ('Water Bottle', 0.99, 1), \
    ('Orange Soda', 1.70, 1), \
    ('Iced Tea', 2.00, 1),  \
    ('Potato Chips', 1.80, 2),   \
    ('Pretzels', 2.20, 2),       \
    ('Popcorn', 1.99, 2),      \
    ('Granola Bar', 1.50, 2),  \
    ('Cookies', 3.00, 2),     \
    ('Cheese', 4.50, 3),   \
    ('Yogurt', 1.25, 3),  \
    ('Butter', 3.75, 3), \
    ('Cream Cheese', 2.50, 3),\
    ('Ice Cream', 5.00, 3), \
    ('Banana', 1.20, 4),  \
    ('Grapes', 2.99, 4), \
    ('Mango', 1.75, 4),  \
    ('Pineapple', 3.00, 4),  \
    ('Strawberries', 2.80, 4); ")
    cursor.execute("\
    INSERT INTO nutritions (products_id, name, calories, fats, sugar) VALUES\
        (1, 'Orange Juice', 120, 0.2, 20),\
        (2, 'Chocolate Bar', 220, 12, 18),\
        (3, 'Milk', 150, 8, 12),\
        (4, 'Apple', 95, 0.3, 19),\
        (5, 'Carrot', 41, 0.1, 5),\
        (6, 'Coca Cola', 140, 0, 39),   \
        (7, 'Pepsi', 150, 0, 41),      \
        (8, 'Water Bottle', 0, 0, 0),    \
        (9, 'Orange Soda', 160, 0, 44),   \
        (10, 'Iced Tea', 90, 0, 23),    \
        ( 11, 'Potato Chips', 160, 10, 1), \
        (12, 'Pretzels', 110, 1, 1),  \
        (13, 'Popcorn', 120, 5, 0),  \
        (14, 'Granola Bar', 150, 6, 7), \
        (15, 'Cookies', 250, 12, 18), \
        (16, 'Cheese', 113, 9, 1), \
        (17, 'Yogurt', 80, 1.5, 11),  \
        ( 18, 'Butter', 100, 11, 0),   \
        (19, 'Cream Cheese', 99, 10, 1),  \
        (20, 'Ice Cream', 270, 14, 28),\
        (21, 'Banana', 105, 0.3, 14),  \
        (22, 'Grapes', 62, 0.3, 15),  \
        (23, 'Mango', 99, 0.6, 23), \
        (24, 'Pineapple', 50, 0.1, 10),  \
        (25, 'Strawberries', 53, 0.5, 8); ")
    cursor.execute("INSERT INTO orders (time_date, address, customer_name, customer_ph, total_price) VALUES\
    ('2024-09-17 10:30', '123 Main St', 'John Doe', '555-1234', 30.08),\
    ('2024-09-17 11:45', '456 Oak St', 'Jane Smith', '555-5678', 20.13),\
    ('2024-09-17 12:15', '789 Pine St', 'Emily Davis', '555-8765', 22.22),\
    ('2024-09-17 13:00', '321 Elm St', 'Michael Johnson', '555-4321', 15.15),\
    ('2024-09-17 13:30', '654 Maple St', 'Sarah Wilson', '555-6789', 30.99);")
    cursor.execute("INSERT INTO products_orders (order_id, products_id, amount) VALUES\
    (1, 1, 2),\
    (1, 2, 1),\
    (2, 3, 1),\
    (3, 4, 3),\
    (4, 5, 5),\
    (5, 1, 1),\
    (5, 3, 2),\
    (5, 4, 2),\
    (1, 6, 3), \
    (1, 11, 1),\
    (2, 7, 2), \
    (2, 12, 2),\
    (3, 8, 1), \
    (3, 13, 2),\
    (4, 9, 1),\
    (4, 14, 2),\
    (5, 10, 1), \
    (5, 15, 1),\
    (1, 16, 1),\
    (2, 17, 3),\
    (3, 18, 2),\
    (4, 19, 1),\
    (5, 20, 1), \
    (1, 21, 4), \
    (2, 22, 2),\
    (3, 23, 3),\
    (4, 24, 1), \
    (5, 25, 2); ")
    conn.commit()
    conn.close()
