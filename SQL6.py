import sqlite3
from SQL6_def import create_table

create_table()
conn = sqlite3.connect('test_sql.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

'''A'''
'''
d. כתוב את השאילתות הבאות:
i. הצג את כל הפריטים ואת הערך התזונתי שלהם + הקטגוריה שלהם
'''
cursor.execute("SELECT \
    products.products_id AS Product_ID, \
    products.name AS Product_Name, \
    category.name AS Category_Name, \
    nutritions.name AS Nutrition_Name, \
    nutritions.calories AS Calories, \
    nutritions.fats AS Fats, \
    nutritions.sugar AS Sugar \
FROM \
    products \
JOIN \
    category ON products.category_id = category.category_id \
LEFT JOIN \
    nutritions ON products.products_id = nutritions.products_id;")

print('1:')
rows = cursor.fetchall()
for row in rows:
    print(dict(row))
print()
'''
ii. הצג את כל ההזמנות, ובכל הזמנה הצג את כל פרטי המוצר
'''
new_product_id = 1
cursor.execute("""
INSERT OR IGNORE INTO products_orders (order_id, products_id, amount)
SELECT order_id, ?, 1
FROM orders;
""", (new_product_id,))
conn.commit()
cursor.execute("""
SELECT orders.order_id, products.name AS Product_Name, products_orders.amount
FROM orders
JOIN products_orders ON orders.order_id = products_orders.order_id
JOIN products ON products_orders.products_id = products.products_id
ORDER BY orders.order_id;
""")
print('2:')
rows = cursor.fetchall()
for row in rows:
    print(dict(row))
'''iii. הוסף מוצר נוסף לכל הזמנה, INSERT'''
new_product_id = 1
cursor.execute("""
INSERT OR IGNORE INTO products_orders (order_id, products_id, amount)
SELECT order_id, ?, 1
FROM orders;
""", (new_product_id,))
conn.commit()
print('3.נעשה. ')
'''iv. עדכן את עלות כל ההזמנות )כמות X מחיר המוצר(, השתמש ב - UPDATE'''
cursor.execute('''UPDATE orders 
SET total_price = (
SELECT sum( products.price * products_orders.products_id )
FROM products_orders
JOIN products on products_orders.products_id = products.products_id
WHERE products_orders.order_id = orders.order_id
)''')
conn.commit()
cursor.execute("SELECT order_id, total_price FROM orders")
print('4:')
rows = cursor.fetchall()
for row in rows:
    print(dict(row))
'''v. מהי ההזמנה הכי יקרה? הכי זולה? ממוצע?'''
cursor.execute('''SELECT 
max(total_price),
min(total_price),
avg(total_price)
FROM orders;''')
print('5:')
rows = cursor.fetchall()
for row in rows:
    print(dict(row))
'''vi. מי הלקוח שהזמין הכי הרבה פעמים?'''
cursor.execute('''SELECT count(order_count)
FROM (
SELECT max( order_id ) as order_count
FROM products_orders
GROUP by order_id
) ;
''')
print('6:')
rows = cursor.fetchall()
for row in rows:
    print(dict(row))
'''vii. איזה מוצר נמכר הכי הרבה? הכי פחות? ממוצע?'''
cursor.execute('''SELECT p.name, SUM(po.amount) AS total_sold
FROM products p
JOIN products_orders po ON p.products_id = po.products_id
GROUP BY p.products_id
ORDER BY total_sold DESC
LIMIT 1;
''')
print('7:')
print("המוצר שנמכר הכי הרבה:")
rows = cursor.fetchall()
for row in rows:
    print(dict(row))
cursor.execute('''SELECT p.name, SUM(po.amount) AS total_sold
FROM products p
JOIN products_orders po ON p.products_id = po.products_id
GROUP BY p.products_id
ORDER BY total_sold ASC
LIMIT 1;
''')
print("המוצר שנמכר הכי פחות:")
rows = cursor.fetchall()
for row in rows:
    print(dict(row))
cursor.execute('''SELECT AVG(total_sold) AS average_sold
FROM (
    SELECT SUM(po.amount) AS total_sold
    FROM products_orders po
    GROUP BY po.products_id
) AS subquery;
''')
print("הממוצע של כל המוצרים שנמכרו:")
rows = cursor.fetchall()
for row in rows:
    print(dict(row))
'''viii. איזה קטגוריה של מוצרים נמכרים הכי הרבה? הכי פחות?'''
cursor.execute('''SELECT c.name AS category_name, SUM(po.amount) AS total_sold
FROM category c
JOIN products p ON c.category_id = p.category_id
JOIN products_orders po ON p.products_id = po.products_id
GROUP BY c.category_id
ORDER BY total_sold DESC
LIMIT 1;
''')
print('8:')
print("איזו קטגוריה נמכרה הכי הרבה:")
rows = cursor.fetchall()
for row in rows:
    print(dict(row))
cursor.execute('''SELECT c.name AS category_name, SUM(po.amount) AS total_sold
FROM category c
JOIN products p ON c.category_id = p.category_id
JOIN products_orders po ON p.products_id = po.products_id
GROUP BY c.category_id
ORDER BY total_sold ASC
LIMIT 1;
''')
print("איזו קטגוריה נמכרה הכי פחות:")
rows = cursor.fetchall()
for row in rows:
    print(dict(row))
