import psycopg2

def get_connection():
    conn = {
        "host": "127.0.0.1",
        "database" : "library_db",
        "user" : "postgres",
        "password": "your_secure_password",
        "port": 5432
    }
    return psycopg2.connect(**conn)