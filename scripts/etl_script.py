"""
etl_script.py
Author: Mohamed Shafik
Purpose: Simple ETL example for 100x Data Engineer Assessment
"""

import pandas as pd

# Extract process
customers = pd.read_csv("data/customers.csv")

# Transform process
customers["full_name"] = customers["first_name"] + " " + customers["last_name"]

# Load  process
print("Transformed Data:")
print(customers.head())
