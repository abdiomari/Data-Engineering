import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB = {
    "host" : os.getenv("host"),
    "database" : os.getenv("database_name"),
    "user" : os.getenv("user"),
    "password" : os.getenv("password"),
    "port" : os.getenv("port", "5432"),
}

print(DB)

if not all(DB.values()):
    print(DB.values())
    raise ValueError(" MIssing database connection credentials")

def get_connection():
    return psycopg2.connect(**DB)