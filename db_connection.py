import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="client_query_db",
        user="postgres",
        password="vicky@123"
    )
    return conn
