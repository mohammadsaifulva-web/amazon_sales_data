import pandas as pd
import numpy as np

np.random.seed(42)
n_rows = 1000

categories = ['Electronics', 'Home & Kitchen', 'Health & Beauty', 'Sports & Outdoors', 'Others']
category_weights = [0.342, 0.287, 0.189, 0.106, 0.076]

products = [
    'Wireless Earbuds', 'Smart Watch', 'Bluetooth Speaker', 'Kitchen Blender',
    'LED Desk Lamp', 'Running Shoes', 'Water Bottle', 'Backpack', 'Air Fryer', 'Phone Case'
]

regions = ['North America', 'Europe', 'Asia', 'Others']
region_weights = [0.341, 0.294, 0.247, 0.118]

inventory_statuses = ['In Stock', 'Low Stock', 'Out of Stock']
stock_weights = [0.723, 0.185, 0.092]

data = {
    'Order_ID': [f'AMZ-{10000 + i}' for i in range(n_rows)],
    'Date': pd.date_range(start='2024-01-01', end='2025-12-31', periods=n_rows),
    'Category': np.random.choice(categories, n_rows, p=category_weights),
    'Product_Name': np.random.choice(products, n_rows),
    'Region': np.random.choice(regions, n_rows, p=region_weights),
    'Units_Sold': np.random.randint(1, 20, n_rows),
    'Price_Per_Unit': np.random.uniform(15.0, 300.0, n_rows),
    'Profit_Margin': np.random.uniform(0.15, 0.35, n_rows),
    'Inventory_Status': np.random.choice(inventory_statuses, n_rows, p=stock_weights)
}

df = pd.DataFrame(data)

df['Total_Revenue'] = (df['Units_Sold'] * df['Price_Per_Unit']).round(2)
df['Total_Profit'] = (df['Total_Revenue'] * df['Profit_Margin']).round(2)

df.to_csv('amazon_sales_data.csv', index=False)
print("amazon_sales_data.csv generated successfully!")