# -*- coding: utf-8 -*-
"""Natural-Language-To-SQL-FOR-CSV.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A4MA6QJtkTzgEzUmZ0CKfVYrB6ERn2BL
"""

import sqlite3
import pandas as pd
import random

conn = sqlite3.connect('tables.db') # Connecting to the database
cursor = conn.cursor() # Object to run queries

df = pd.read_csv('get_active_users.csv')
df.info()

table_name = 'table'+str(random.randint(1, 100000))


columns_with_types = ", ".join([f"{col.replace(' ', '_')} TEXT" for col in df.columns])
create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types});"

cursor.execute(create_table_query)
cursor.fetchall()

for index, row in df.iterrows():
    values = ", ".join([f'"{row_item}"' for row_item in row])
    insert_sql = f"INSERT INTO {table_name} ({', '.join(df.columns.str.replace(' ', '_'))}) VALUES ({values})"
    cursor.execute(insert_sql)

cursor.execute('SELECT COUNT(*) FROM '+table_name)
cursor.fetchall()