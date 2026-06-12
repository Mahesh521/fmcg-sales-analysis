import psycopg2
import pandas as pd
from db import engine

query = """
    SELECT * FROM fmcg_sales;
"""

df = pd.read_sql(query, engine)

print(df)
print(df.shape)
print(df.dtypes)
print(df.head())


