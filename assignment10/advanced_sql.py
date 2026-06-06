import sqlite3
from datetime import date

DB_PATH = "../db/lesson.db"
conn = sqlite3.connect(DB_PATH)
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()


# ----------------------------------------------#
# Task 1 - total price for each order
query = """
SELECT o.order_id, sum(price * quantity) as Total
FROM orders o 
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id LIMIT 5
;
"""

cursor.execute(query)
print("query 1: ", cursor.fetchall())

# ----------------------------------------------#
# Task 2 - average price of orders for each customer
query = """
WITH order_prices AS (
    SELECT o.customer_id, sum(price * quantity) as total
    FROM orders o 
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY o.order_id
)
SELECT c.customer_name, avg(total)
FROM order_prices op JOIN customers c ON op.customer_id = c.customer_id
GROUP BY op.customer_id
;
"""

cursor.execute(query)
print("query 2: ", cursor.fetchall())


# ----------------------------------------------#
# Task 4
# Find all employees associated with more than 5 orders.  You want the first_name, the last_name, and the count of orders

query = """
SELECT e.first_name, e.last_name, count(order_id) as totals
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id
HAVING totals > 5
ORDER BY totals DESC
;
"""

cursor.execute(query)
print("query 4: ", cursor.fetchall())


# ----------------------------------------------#
# Task 3 - new order transaction for customer Perez and Sons. employee Miranda Harris. 
# Order of 10 of each of the 5 least expensive products

# query for customer id
cursor.execute("SELECT customer_id FROM customers WHERE customer_name = ?", ("Perez and Sons",))
results = cursor.fetchall()
if len(results) > 0: 
    customer_id = results[0][0]

# query for employee id
cursor.execute("SELECT employee_id FROM employees WHERE first_name = ? AND last_name = ?", ("Miranda", "Harris",))
results = cursor.fetchall()
if len(results) > 0: 
    employee_id = results[0][0]

# query for least expensive products
cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT ?", (5,))
results = cursor.fetchall()
if len(results) > 0: 
    products = [i[0] for i in results]


# create new order, transaction start
try:
    # adding a new record to orders table
    cursor.execute("INSERT INTO orders (customer_id, employee_id, date) VALUES (?,?,?) RETURNING order_id", (customer_id, employee_id, date.today()))
    results = cursor.fetchall()
    order_id = results[0][0]

    # adding a new record to line_items table with the same order id
    for i in products: 
        cursor.execute("INSERT INTO line_items (order_id, product_id, quantity) VALUES (?,?,?)", (order_id, i, 10))
    
    conn.commit()  # Commit transaction
    print("New order created successfully")
except Exception as e:
    conn.rollback()  # Rollback transaction if there's an error
    print("Error:", e)


conn.close()
