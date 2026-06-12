import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="fmcg_sales",
    user="postgres",
    password="Kavya@99",
    port="5432"
)

print("Connection successful!")
conn.close()