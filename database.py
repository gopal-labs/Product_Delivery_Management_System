import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="delivery_system",
        user="postgres",
        password="335512"
    )

    cursor = conn.cursor()

    print("Database connected successfully")

except Exception as e:
    print("Connection failed")
    print(e)