import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create a sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert sample data
sales_data = [
    ('Product A', 30, 10.5),
    ('Product B', 20, 15.0),
    ('Product C', 50, 8.0),
    ('Product A', 10, 10.5),
    ('Product B', 15, 15.0),
    ('Product C', 25, 8.0),
]
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sales_data)

conn.commit()
conn.close()

print("Database created and populated with sample data!")
