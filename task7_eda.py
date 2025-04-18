import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect("sales_data.db")

# Query to calculate total quantity and revenue
query = """
SELECT 
    product, 
    SUM(quantity) AS total_quantity, 
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
"""

# Execute query and load results into a DataFrame
df = pd.read_sql_query(query, conn)

# Print results
print("Sales Summary:")
print(df)

# Plot bar chart for revenue by product
df.plot(kind='bar', x='product', y='total_revenue', color='skyblue', legend=False)
plt.title('Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.savefig('revenue_by_product.png')  # Save the chart as a PNG file
plt.show()

# Plot bar chart for quantity by product
df.plot(kind='bar', x='product', y='total_quantity', color='orange', legend=False)
plt.title('Quantity Sold by Product')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.savefig('quantity_by_product.png')  # Save the chart as a PNG file
plt.show()

conn.close()
