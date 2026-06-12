import psycopg2
import pandas as pd

from db import engine
query = """
    SELECT * FROM fmcg_sales;
"""

df = pd.read_sql(query, engine)


# Shape
print("Shape:",df.shape)

#Data Types
print("\nData Types:")
print(df.dtypes)

#Null Values
print("\nNUll Values:")
print(df.isnull().sum())

#Duplicates
print("\nDuplicate Rows:",df.duplicated().sum())

#Basic Stats
print("\nBasic Stats:")
print(df.describe())