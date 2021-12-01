import psycopg2
conn = psycopg2.connect(user="postgres", password="123456", database="demo", host="localhost", port="5432")
print("Successfully connected!")